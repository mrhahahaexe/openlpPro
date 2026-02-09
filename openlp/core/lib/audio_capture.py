# -*- coding: utf-8 -*-

##########################################################################
# OpenLP - Open Source Lyrics Projection                                 #
# ---------------------------------------------------------------------- #
# Copyright (c) 2008 OpenLP Developers                                   #
# ---------------------------------------------------------------------- #
# This program is free software: you can redistribute it and/or modify   #
# it under the terms of the GNU General Public License as published by   #
# the Free Software Foundation, either version 3 of the License, or      #
# (at your option) any later version.                                    #
#                                                                        #
# This program is distributed in the hope that it will be useful,        #
# but WITHOUT ANY WARRANTY; without even the implied warranty of         #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          #
# GNU General Public License for more details.                           #
#                                                                        #
# You should have received a copy of the GNU General Public License      #
# along with this program.  If not, see <https://www.gnu.org/licenses/>. #
##########################################################################
"""
The :mod:`~openlp.core.lib.audio_capture` module provides audio capture capabilities.
"""
import logging
import threading
import numpy as np
import sounddevice as sd
import soundfile as sf
from io import BytesIO

from PySide6 import QtCore

log = logging.getLogger(__name__)

class AudioCaptureService(QtCore.QObject):
    """
    Service to capture audio from the microphone for AI recognition.
    """
    recording_finished = QtCore.Signal(bytes)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.is_recording = False
        self.sample_rate = 44100
        self.channels = 1
        self.recording_data = []
        self.stream = None

    def start_recording(self, duration=10):
        """
        Start recording for a specified duration in seconds.
        """
        if self.is_recording:
            return
        
        log.debug("Starting audio recording...")
        self.is_recording = True
        self.recording_data = []
        
        # Start recording in a separate thread to not block the UI
        threading.Thread(target=self._record, args=(duration,), daemon=True).start()

    def _record(self, duration):
        try:
            recording = sd.rec(int(duration * self.sample_rate), 
                              samplerate=self.sample_rate, 
                              channels=self.channels)
            sd.wait()  # Wait for recording to finish
            
            if self.is_recording:
                # Convert to WAV in memory
                buffer = BytesIO()
                sf.write(buffer, recording, self.sample_rate, format='WAV')
                audio_bytes = buffer.getvalue()
                
                log.debug("Recording finished, sending data...")
                self.recording_finished.emit(audio_bytes)
        except Exception:
            log.exception("Error during audio recording")
        finally:
            self.is_recording = False

    def stop_recording(self):
        """
        Stop the current recording.
        """
        if not self.is_recording:
            return
        
        self.is_recording = False
        sd.stop()
        log.debug("Audio recording stopped manually.")
