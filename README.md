## Click button, receive log message

This Android app project can be executed with Briefcase. Try downloading it,
then running:

```bash
$ briefcase create android
$ briefcase build android
$ briefcase run android -d emulator-5554
```

You'll need a **Python 3.7 virtualenv** as well as briefcase from current git.

Once you launch the app, I recommend running this to see the output.

```bash
$ ~/.briefcase/tools/android_sdk/platform-tools/adb logcat
```
