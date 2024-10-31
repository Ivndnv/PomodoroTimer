import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import QUrl, QSize, QFile, QObject, Qt, QTime, QThread, SignalInstance, Signal
from PySide6.QtMultimedia import QMediaPlayer, QAudio, QAudioOutput
from pomodoro_gui import Ui_MainWindow
from about import Ui_AboutWindow
import time as t


def resource_path(relative_path: str) -> str:
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath('.')

    return os.path.join(base_path, relative_path)


class Thread(QThread):

    def __init__(self):
        super(Thread, self).__init__()

        self.func = None

    def stop(self):
        self.terminate()

    def run(self):
        self.working = True
        while self.working:
            self.func()
        else:
            self.msleep(100)

    def resume(self):
        self.working = True

    def pause(self):
        self.working = False


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.timeEdit.setTime(QTime(0, 5, 0))
        time = self.ui.timeEdit.time()
        self.ui.TimerLabel.setText(time.toString('mm:ss'))
        self.ui.timeEdit.timeChanged.connect(self.set_time)
        self.ui.timeEdit.setMinimumTime(QTime(0, 0, 0))
        self.action_open_about = QAction('?', self)
        self.ui.menuBar.addAction(self.action_open_about)
        self.action_open_about.triggered.connect(self.open_about)
        self.ui.StartTimerButton.clicked.connect(self.timer_btn_click)
        self.ui.StopTimerButton.clicked.connect(self.reset)
        self.ui.PomodoroTimerButton.clicked.connect(self.pomodoro_btn_click)
        self.ui.VolumeSlider.valueChanged.connect(self.set_volume)
        self.ui.VolumeSlider.valueChanged.connect(self.play_audio)
        self.ui.VolumeCheckBox.checkStateChanged.connect(self.mute)
        self.audio = QAudioOutput()
        self.audio.setVolume(float(self.ui.VolumeSlider.value()))
        self.player = QMediaPlayer()
        self.player.setAudioOutput(self.audio)
        self.player.setSource(QUrl.fromLocalFile(
            resource_path('mediafiles/End sound.mp3')))

        icon1 = QIcon()
        icon1.addFile(resource_path("mediafiles/play.ico"), QSize(),
                      QIcon.Mode.Active, QIcon.State.Off)
        icon1.addFile(resource_path("mediafiles/pause.ico"), QSize(),
                      QIcon.Mode.Active, QIcon.State.On)
        self.ui.StartTimerButton.setIcon(icon1)
        icon2 = QIcon()
        icon2.addFile(resource_path("mediafiles/restart.ico"), QSize(),
                      QIcon.Mode.Normal, QIcon.State.Off)
        self.ui.StopTimerButton.setIcon(icon2)
        icon3 = QIcon()
        icon3.addFile(resource_path("mediafiles/pomodoro_icon.ico"),
                      QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.setWindowIcon(icon3)
        self.ui.PomodoroTimerButton.setIcon(icon3)

        self.th = Thread()
        self.thread_for_audio = Thread()

    def mute(self):
        if self.ui.VolumeCheckBox.isChecked():
            self.ui.VolumeSlider.setEnabled(True)
            self.set_volume()
        else:
            self.ui.VolumeSlider.setEnabled(False)
            self.set_volume(0.0)

    def real_vol(self, slider_value=None):
        slider_value = self.ui.VolumeSlider.value()
        return QAudio.convertVolume(
            slider_value*0.01,
            QAudio.VolumeScale.LogarithmicVolumeScale,
            QAudio.VolumeScale.LinearVolumeScale
        )

    def set_volume(self, vol=None):
        if vol == None:
            vol = self.real_vol()

        self.audio.setVolume(vol * 0.01)

    def play_audio(self):
        self.player.play()

    def timer_btn_click(self):
        if self.ui.StartTimerButton.isChecked():
            self.th.func = self.countdown
            self.th.resume()
            self.th.start(priority=QThread.Priority.LowPriority)
        else:
            self.th.pause()

    def pomodoro_btn_click(self):
        self.th.func = self.pomodoro
        self.th.start(priority=QThread.Priority.LowPriority)

    def set_time(self) -> None:
        Time = self.ui.timeEdit.time()
        self.ui.TimerLabel.setText(Time.toString('mm:ss'))

    def update_time(self, time: QTime) -> None:
        self.ui.TimerLabel.setText(time.toString('mm:ss'))

    def get_time(self) -> QTime:
        return QTime.fromString(self.ui.TimerLabel.text(), 'mm:ss')

    def countdown(self, time: QTime = None) -> None:
        if time == None:
            time = self.get_time()
        else:
            self.update_time(time=time)
        if self.ui.StartTimerButton.isChecked():
            self.th.resume()
            while time != QTime(0, 0, 0, 0):
                if self.th.working:
                    time = self.get_time()
                    time = time.addSecs(-1)
                    self.update_time(time=time)
                    t.sleep(1)
            else:
                self.th.pause()

        self.ui.StartTimerButton.setChecked(False)
        self.play_audio()

    def reset(self):
        if self.th.isRunning():
            self.th.blockSignals(True)
            self.th.terminate()
            self.th.blockSignals(False)
        if self.ui.StartTimerButton.isChecked():
            self.ui.StartTimerButton.setChecked(False)
        if not self.ui.StartTimerButton.isEnabled():
            self.ui.StartTimerButton.setEnabled(True)
        self.set_time()

    def pomodoro(self):
        self.ui.StartTimerButton.setEnabled(False)
        for _ in range(2):
            # 25 min

            self.ui.StartTimerButton.setChecked(True)
            self.countdown(time=QTime(0, 25, 0))
            self.ui.StartTimerButton.setChecked(False)

            t.sleep(1.5)

            # 5 min
            self.ui.StartTimerButton.setChecked(True)
            self.countdown(time=QTime(0, 5, 0))
            self.ui.StartTimerButton.setChecked(False)

            t.sleep(1.5)

    def open_about(self):
        self.about_window = AboutWindow()
        self.about_window.show()


class AboutWindow(QWidget):
    def __init__(self) -> None:
        super(AboutWindow, self).__init__()
        self.ui = Ui_AboutWindow()
        self.ui.setupUi(self)
        icon = QIcon()
        icon.addFile(resource_path("mediafiles/pomodoro_icon.ico"),
                     QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.setWindowIcon(icon)
        self.ui.AboutText.setTextFormat(Qt.TextFormat.RichText)
        self.ui.AboutText.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextBrowserInteraction)
        self.ui.AboutText.setOpenExternalLinks(True)
        self.ui.gridLayout.addWidget(
            self.ui.pushButton, 2, 0, 1, 1, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.ui.pushButton.clicked.connect(self.destroy)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
