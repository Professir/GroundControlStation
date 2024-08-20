import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QComboBox
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from connection import ArduPilotConnection

class Worker(QThread):
    data_signal = pyqtSignal(dict)
    
    def __init__(self, address="udpin:localhost:14551"):
        super().__init__()
        self.connection = ArduPilotConnection(address)
        self.running = True

    def run(self):
        while self.running:
            data = self.connection.fetch_data()
            if data:
                self.data_signal.emit(data)

    def stop(self):
        self.running = False

class GCSMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sigma GCS")
        self.setGeometry(100, 100, 1200, 800)
        self.setStyleSheet("background-color: #1e1f1e; color: white") 
        self.initUI()
        self.start_worker()

    def initUI(self):
        self.main_widget = QWidget()
        self.main_layout = QHBoxLayout()

        # Sol Panel
        self.left_panel = QVBoxLayout()
        # self.left_panel.addWidget(self.createCompassWidget("ABSOLUTE"))
        self.left_panel.addWidget(self.createSpeedWidget())
        self.left_panel.addWidget(self.createFailSafeButton())
        
        # Orta Panel
        self.center_panel = QVBoxLayout()
        self.center_panel.addWidget(self.createVideoFeed())
        self.center_panel.addWidget(self.createBatteryWidget())
        self.center_panel.addWidget(self.createFlightTimeWidget())
        
        # Sağ Panel
        self.right_panel = QVBoxLayout()
        # self.right_panel.addWidget(self.createCompassWidget("RELATIVE"))
        self.right_panel.addWidget(self.createActionModeWidget())
        self.right_panel.addWidget(self.createRecordingWidget())
        self.right_panel.addWidget(self.createStatusLogWidget())
        self.right_panel.addWidget(self.createFailSafeButton())

        self.main_layout.addLayout(self.left_panel)
        self.main_layout.addLayout(self.center_panel)
        self.main_layout.addLayout(self.right_panel)
        
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)

    # def createCompassWidget(self, title):
    #     compass_widget = QWidget()
    #     compass_layout = QVBoxLayout()
        
    #     title_label = QLabel(title)
    #     title_label.setAlignment(Qt.AlignCenter)
    #     compass_layout.addWidget(title_label)
        
    #     compass_label = QLabel()
    #     pixmap = QPixmap('compass.png')  # Replace with your compass image path
    #     compass_label.setPixmap(pixmap)
    #     compass_label.setAlignment(Qt.AlignCenter)
    #     compass_layout.addWidget(compass_label)
        
    #     compass_widget.setLayout(compass_layout)
    #     return compass_widget

    def createSpeedWidget(self):
        self.speed_widget = QWidget()
        self.speed_layout = QVBoxLayout()

        self.ground_speed = QLabel("GROUND SPEED (m/s)\n")
        self.air_speed = QLabel("AIR SPEED (m/s)\n")
        self.speed_mean = QLabel("SPEED MEAN (m/s)\n")
        self.altitude = QLabel("ALTITUDE (m)\n")
        
        self.speed_layout.addWidget(self.ground_speed)
        self.speed_layout.addWidget(self.air_speed)
        self.speed_layout.addWidget(self.speed_mean)
        self.speed_layout.addWidget(self.altitude)
        
        self.speed_widget.setLayout(self.speed_layout)
        return self.speed_widget
    
    def createBatteryWidget(self):
        self.minimal_widget = QWidget()
        self.minimal_layout = QHBoxLayout()
        
        self.battery_label = QLabel("Battery Remaining: N/A")

        # self.battery_label.setFixedSize(180, 120)
        self.battery_label.setAlignment(Qt.AlignCenter)

        self.minimal_layout.addWidget(self.battery_label)
        
        self.minimal_widget.setLayout(self.minimal_layout)
        return self.battery_label

    def createFailSafeButton(self):
        fail_safe_button = QPushButton("FAILSAFE")
        fail_safe_button.setStyleSheet("background-color: red; color: white; font-size: 20px;")
        return fail_safe_button

    def createVideoFeed(self):
        video_widget = QLabel()
        video_widget.setStyleSheet("background-color: black;")
        video_widget.setFixedSize(640, 360)
        video_widget.setAlignment(Qt.AlignCenter)
        video_widget.setText("Video Feed")
        return video_widget

    def createFlightTimeWidget(self):
        self.flight_time_widget = QLabel("FLIGHT TIME: 00:00:00")
        self.flight_time_widget.setAlignment(Qt.AlignCenter)
        return self.flight_time_widget

    def createActionModeWidget(self):
        action_mode_widget = QWidget()
        action_layout = QVBoxLayout()

        action_mode_label = QLabel("SET ACTION / MODE")
        action_mode_label.setAlignment(Qt.AlignCenter)
        # action_mode_label.setFixedSize(160, 80)
        action_layout.addWidget(action_mode_label)
        
        action_mode_combobox = QComboBox()
        action_mode_combobox.addItem("Manual")
        action_mode_combobox.addItem("Auto")
        action_layout.addWidget(action_mode_combobox)
        
        set_button = QPushButton("SET")
        action_layout.addWidget(set_button)
        
        action_mode_widget.setLayout(action_layout)
        return action_mode_widget

    def createRecordingWidget(self):
        recording_widget = QWidget()
        recording_layout = QVBoxLayout()

        recording_label = QLabel("RECORDING")
        recording_label.setAlignment(Qt.AlignCenter)
        recording_layout.addWidget(recording_label)
        
        start_pause_button = QPushButton("START / PAUSE")
        stop_button = QPushButton("STOP")
        recording_layout.addWidget(start_pause_button)
        recording_layout.addWidget(stop_button)
        
        recording_widget.setLayout(recording_layout)
        return recording_widget

    def createStatusLogWidget(self):
        status_log_widget = QLabel()
        status_log_widget.setStyleSheet("background-color: black; color: white;")
        status_log_widget.setFixedSize(300, 150)
        status_log_widget.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        status_log_widget.setText("Status Log:\n...")
        return status_log_widget


    def start_worker(self):
        self.worker = Worker()
        self.worker.data_signal.connect(self.update_ui)
        self.worker.start()

    def update_ui(self, data):
        if 'battery' in data:
            # self.status_log_widget.setText(f"Batarya Yüzdesi: {data['battery']:.1f}")
            self.battery_label.setText(f"Batarya Yüzdesi: {data['battery']:.1f}%")
        if 'ground_speed' in data:
            self.ground_speed.setText(f"GROUND SPEED (m/s)\n{data['ground_speed']:.1f}")
        if 'air_speed' in data:
            self.air_speed.setText(f"AIR SPEED (m/s)\n{data['air_speed']:.1f}")
        if 'speed_mean' in data:
            self.speed_mean.setText(f"SPEED MEAN (m/s)\n{data['speed_mean']:.1f}")
        if 'altitude' in data:
            self.altitude.setText(f"ALTITUDE (m)\n{data['altitude']:.1f}")
        if 'flight_time' in data:
            self.flight_time_widget.setText(f"FLIGHT TIME: {self.format_time(data['flight_time'])}")
        # if 'throttle' in data:
        #     self.altitude.setText(f'ALTITUDE (m)\n{data['throttle']}')

    def format_time(self, seconds):
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        seconds = int(seconds % 60)
        return f"{hours:02}:{minutes:02}:{seconds:02}"

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GCSMainWindow()
    window.show()
    sys.exit(app.exec_())
