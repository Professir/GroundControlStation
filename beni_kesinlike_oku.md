<!-- Tasarimin suanlik berbat oldugunun ve eksiklerinin oldugunun farkindayim bastan daha duzenli ve guzel eksikleri tamamlayici sekilde yapmaya calisiyorum ancak bugune yetisen bu oldu sry :( -->

# Sanirsam bir eksik yok her seyi buraya yazdim ama eger olursa bana (+90) 544 330 9345 telefon numarasiyla whatsapp veya direkt arayarak ulasabilirsiniz. Yaninizda olamadigim icin uzgunum :)

Baslatmak icin Simulasyonu bagladiktan sonra GCS.py dosyasini calistirmak 
yeterli olacaktir.

# Ardupilotta denemek istiyorsaniz

# ../Tools/autotest/sim_vehicle.py -v ArduCopter --console --map --out=udp:localhost:14551
yukaridaki console koduyla sadece sizdeki sim_vehicle.py dosyasi hangi dizindeyse onu duzenleyip baslatabilirsiniz.

# Eger pixhawk usb port ile baglarsaniz adress olarak sanirsam assagidaki adress dogru olacaktir.
/dev/ttyACM0 



# !!!!Duzeltilmesi gerekebilecek seyler!!!!!

1) connection.py dosyasinda altitude verisinden bi' cikarma islemi yapiyorum cunku simulasyonda yukseklik olarak 584 metre referans aliyor pixhawk baglandiginda o duzeltilmesi gerekir.
2) QtWebEngineWidgets'i linux'a kuramadim hata aldim o yuzden onu koddan cikarmak zorunda kaldim. create_map.py dosyasiyla ilettigim map olusturma kodunu bir kez calistirdak sonra:
# from PyQt5.QtWebEngineWidgets import QWebEngineView
bunu import edip, orta panel kisminda videofeed'in hemen altina  
# center_panel.addWidget(self.createMapView())  
bunu import etmek ve
kodun herhangi bir kismina assagida bulunan fonksiyonu eklemek yeterli olacaktir 
#    def createMapView(self):
#        map_view = QWebEngineView()
#        map_view.load(QtCore.QUrl("file:///" + QtCore.QDir.current().absoluteFilePath("drone_map.html")))  # Haritanın tam yolu
#        map_view.setFixedSize(640, 360)  # boyut ayari
#        return map_view

3) kodda bulunan yorum satirindaki compass kisimlari png olarak eklemek isterseniz png olarak indirip o satirlari yorum satirindan kaldirip kullanabilirsiniz.


# merak ettiyseniz diye
verileri cekmeyi worker adli arkadasimiz yapiyor qthreadlar olusturarak arka planda calisiyor cok iyi.



# Keyfinize kalan sey

1) eger verilerin hepsi geliyor mu falan ne biliyim bir sey denemek isterseniz data verisinin icerisine veri eklemek isterseniz. Gelen verilerin ciktisi assagidaki gibidir 

AHRS2 {roll : -0.0015635028248652816, pitch : -0.0017778995679691434, yaw : -0.11896120011806488, altitude : 584.0899658203125, lat : -353632621, lng : 1491652374}
ATTITUDE {time_boot_ms : 4726109, roll : -0.001047287485562265, pitch : -0.001252750400453806, yaw : -0.1404491513967514, rollspeed : -0.0001454278826713562, pitchspeed : -0.000352791219484061, yawspeed : -0.0007858731551095843}
GLOBAL_POSITION_INT {time_boot_ms : 4726109, lat : -353632620, lon : 1491652373, alt : 584080, relative_alt : -5, vx : 1, vy : -1, vz : 0, hdg : 35196}
VFR_HUD {airspeed : 0.024010704830288887, groundspeed : 0.024008734151721, heading : 351, throttle : 0, alt : 584.0800170898438, climb : 0.00030756706837564707}
SYS_STATUS {onboard_control_sensors_present : 1399979055, onboard_control_sensors_enabled : 1382128687, onboard_control_sensors_health : 1467063343, load : 0, voltage_battery : 12600, current_battery : 0, battery_remaining : 100, drop_rate_comm : 0, errors_comm : 0, errors_count1 : 0, errors_count2 : 0, errors_count3 : 0, errors_count4 : 0}
POWER_STATUS {Vcc : 5000, Vservo : 0, flags : 0}
MEMINFO {brkval : 0, freemem : 65535, freemem32 : 131072}
NAV_CONTROLLER_OUTPUT {nav_roll : -0.000139205512823537, nav_pitch : 0.00013695219240617007, nav_bearing : -8, target_bearing : 0, wp_dist : 0, alt_error : 0.005918004550039768, aspd_error : 0.0, xtrack_error : 0.0}
MISSION_CURRENT {seq : 0, total : 0, mission_state : 1, mission_mode : 0}
SERVO_OUTPUT_RAW {time_usec : 431142337, port : 0, servo1_raw : 1000, servo2_raw : 1000, servo3_raw : 1000, servo4_raw : 1000, servo5_raw : 0, servo6_raw : 0, servo7_raw : 0, servo8_raw : 0, servo9_raw : 0, servo10_raw : 0, servo11_raw : 0, servo12_raw : 0, servo13_raw : 0, servo14_raw : 0, servo15_raw : 0, servo16_raw : 0}
RC_CHANNELS {time_boot_ms : 4726109, chancount : 8, chan1_raw : 1500, chan2_raw : 1500, chan3_raw : 1000, chan4_raw : 1500, chan5_raw : 1800, chan6_raw : 1000, chan7_raw : 1000, chan8_raw : 1800, chan9_raw : 0, chan10_raw : 0, chan11_raw : 0, chan12_raw : 0, chan13_raw : 0, chan14_raw : 0, chan15_raw : 0, chan16_raw : 0, chan17_raw : 0, chan18_raw : 0, rssi : 255}
RAW_IMU {time_usec : 4726109633, xacc : 0, yacc : 0, zacc : -1001, xgyro : 1, ygyro : 0, zgyro : 1, xmag : 224, ymag : 80, zmag : -528, id : 0, temperature : 4499}
SCALED_IMU2 {time_boot_ms : 4726109, xacc : 0, yacc : 0, zacc : -1001, xgyro : 1, ygyro : 1, zgyro : 1, xmag : 224, ymag : 80, zmag : -528, temperature : 4499}
SCALED_IMU3 {time_boot_ms : 4726109, xacc : 0, yacc : 0, zacc : 0, xgyro : 0, ygyro : 0, zgyro : 0, xmag : 224, ymag : 80, zmag : -528, temperature : 0}
SCALED_PRESSURE {time_boot_ms : 4726109, press_abs : 945.0282592773438, press_diff : 0.0, temperature : 3120, temperature_press_diff : 0}
SCALED_PRESSURE2 {time_boot_ms : 4726109, press_abs : 945.0402221679688, press_diff : 0.0, temperature : 3120, temperature_press_diff : 0}
GPS_RAW_INT {time_usec : 4725963000, fix_type : 6, lat : -353632621, lon : 1491652374, alt : 584090, eph : 121, epv : 200, vel : 0, cog : 0, satellites_visible : 10, alt_ellipsoid : 584090, h_acc : 300, v_acc : 300, vel_acc : 0, hdg_acc : 0, yaw : 0}
SYSTEM_TIME {time_unix_usec : 1721504025946230, time_boot_ms : 4726109}
SIMSTATE {roll : 0.0, pitch : 0.0, yaw : -0.12217313796281815, xacc : 0.0, yacc : 0.0, zacc : -9.806650161743164, xgyro : 0.0, ygyro : 0.0, zgyro : 0.0, lat : -353632621, lng : 1491652374}
WIND {direction : -180.0, speed : 0.0, speed_z : 0.0}
TERRAIN_REPORT {lat : -353632620, lon : 1491652373, spacing : 100, terrain_height : 583.843994140625, current_height : 0.23602294921875, pending : 0, loaded : 504}
EKF_STATUS_REPORT {flags : 831, velocity_variance : 0.008802163414657116, pos_horiz_variance : 0.005082962103188038, pos_vert_variance : 2.957348078780342e-05, compass_variance : 0.014070465229451656, terrain_alt_variance : 0.0, airspeed_variance : 0.0}
LOCAL_POSITION_NED {time_boot_ms : 4726109, x : 0.011035985313355923, y : -0.015033205039799213, z : 0.005918004550039768, vx : 0.014337368309497833, vy : -0.01925770565867424, vz : -0.00030756706837564707}
VIBRATION {time_usec : 4726109633, vibration_x : 0.0025160496588796377, vibration_y : 0.002960322191938758, vibration_z : 0.0028339801356196404, clipping_0 : 0, clipping_1 : 0, clipping_2 : 0}
BATTERY_STATUS {id : 0, battery_function : 0, type : 0, temperature : 32767, voltages : [12600, 65535, 65535, 65535, 65535, 65535, 65535, 65535, 65535, 65535], current_battery : 0, current_consumed : 0, energy_consumed : 0, battery_remaining : 100, time_remaining : 0, charge_state : 1, voltages_ext : [0, 0, 0, 0], mode : 0, fault_bitmask : 0}
ESC_TELEMETRY_1_TO_4 {temperature : [32, 32, 32, 32], voltage : [1679, 1679, 1679, 1679], current : [80, 80, 80, 80], totalcurrent : [1, 1, 1, 1], rpm : [0, 0, 0, 0], count : [53036, 53036, 53036, 53036]}
AHRS {omegaIx : -0.0012648560805246234, omegaIy : -0.0013085141545161605, omegaIz : -0.0018194715958088636, accel_weight : 0.0, renorm_val : 0.0, error_rp : 0.0023467319551855326, error_yaw : 0.0013865060172975063}