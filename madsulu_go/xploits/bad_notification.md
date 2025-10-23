# Bad Notification

Xploit for Madsulu Go based on YouTube.

## About

The July 22nd, 2025 a notification was sent to the app users about the MadSulu Go Cup, an event that was happening on the MadSulu Go YouTube channel.

However, this introduced a vulnerability as tapping the notification opens the YouTube post in the app WebView, meaning that if you find a `google.com` (or any) hyperlink, you'll be able to browse the web.

## Requirements

- Have installed the app before the July 22nd, 2025.
- Not have deleted the in-app notifications.

## Xploit

1. Go to your app notifications
   <br>
   <img src="../../.github/screenshots/badnotification_1.jpeg" width="150">

2. Tap on the MadSulu Go Cup notification
   <br>
   <img src="../../.github/screenshots/badnotification_2.jpeg" width="150">

3. Tap on the search button
   <br>
   <img src="../../.github/screenshots/badnotification_3.jpeg" width="150">

4. Search `www.google.com`
   <br>
   <img src="../../.github/screenshots/badnotification_4.jpeg" width="150">

5. Tap on the first video result
   <br>
   <img src="../../.github/screenshots/badnotification_5.jpeg" width="150">

6. Tap on Description and look for the `www.google.com` links.
   <br>
   <img src="../../.github/screenshots/badnotification_6.jpeg" width="150">

TADA! Now you're on Google 🎉
<br>
<img src="../../.github/screenshots/badnotification_7.jpeg" width="150">

## Notes

This Xploit only allows to escape the app content and browse the web, not to run arbitrary code in the app.
MGH 2.0 allows for arbitrary code execution for there is no ETA for its release.

