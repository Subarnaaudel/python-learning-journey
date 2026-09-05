# 3. install a external module and use it to perform an opeartion of your interest
# for solving this install pip install pyttsx3

import pyttsx3
engine = pyttsx3.init()
engine.say("Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.")

engine.runAndWait()