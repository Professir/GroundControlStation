from pymavlink import mavutil

class ArduPilotConnection:
    def __init__(self, address="udpin:localhost:14551"):
        self.vehicle = mavutil.mavlink_connection(address, baud=57600, autoreconnect=True)
        self.vehicle.wait_heartbeat()
        print("Bağlanti Başarili...")

    def fetch_data(self):
        try:
            data = {}
            msg = self.vehicle.recv_match(blocking=True)
            if msg is not None:
                if msg.get_type() == "BATTERY_STATUS":
                    data['battery'] = msg.battery_remaining
                elif msg.get_type() == "VFR_HUD":
                    data['ground_speed'] = msg.groundspeed
                    data['air_speed'] = msg.airspeed
                    data['altitude'] = msg.alt - 584.1 # Drone'un yerden yukseklik olarak 584 metre referans aliyor
                    data['throttle'] = msg.throttle
                    data['speed_mean'] = (msg.groundspeed + msg.airspeed) / 2
                elif msg.get_type() == "SYSTEM_TIME":
                    data['flight_time'] = msg.time_boot_ms / 1000  # Uçuş süresini saniye cinsinden alıyoruz
                # elif msg.get_type() == "GLOBAL_POSITION_INT":
                #     data[]
            return data
        except Exception as e:
            print(f"Hata: {e}")
            return None
