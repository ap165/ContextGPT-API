LOGIN_OTP = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your ContextGPT Login Code</title>
    <style>
        /* Reset styles for email clients */
        body, table, td, a { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; }
        table, td { mso-table-lspace: 0pt; mso-table-rspace: 0pt; }
        img { -ms-interpolation-mode: bicubic; }
        img { border: 0; height: auto; line-height: 100%; outline: none; text-decoration: none; }
        table { border-collapse: collapse !important; }
        body { height: 100% !important; margin: 0 !important; padding: 0 !important; width: 100% !important; }
        a[x-apple-data-detectors] { color: inherit !important; text-decoration: none !important; font-size: inherit !important; font-family: inherit !important; font-weight: inherit !important; line-height: inherit !important; }
    </style>
</head>
<body style="background-color: #f3f4f6; margin: 0 !important; padding: 0 !important; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;">

    <!-- Wrapper -->
    <table border="0" cellpadding="0" cellspacing="0" width="100%">
        <tr>
            <td align="center" style="padding: 40px 10px 40px 10px;">
                
                <!-- Main Card -->
                <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px; background-color: #ffffff; border-radius: 8px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);">
                    
                    <!-- Header -->
                    <tr>
                        <td align="center" style="padding: 30px 30px 20px 30px; background-color: #0f172a; border-top-left-radius: 8px; border-top-right-radius: 8px;">
                            <h1 style="margin: 0; color: #ffffff; font-size: 24px; font-weight: 700; letter-spacing: 2px;">ContextGPT</h1>
                        </td>
                    </tr>

                    <!-- Body Content -->
                    <tr>
                        <td align="left" style="padding: 40px 30px 20px 30px; color: #333333; font-size: 16px; line-height: 1.6;">
                            <h2 style="margin: 0 0 20px 0; color: #0f172a; font-size: 20px; font-weight: 600;">Log in to your account</h2>
                            <p style="margin: 0 0 20px 0;">Hi <strong>{{USER_NAME}}</strong>,</p>
                            <p style="margin: 0 0 20px 0;">Use the following One-Time Password (OTP) to securely log in to your ContextGPT account. This code is valid for the next <strong>10 minutes</strong>.</p>
                        </td>
                    </tr>

                    <!-- OTP Box (Light Blue/Crypto Theme) -->
                    <tr>
                        <td align="center" style="padding: 10px 30px 30px 30px;">
                            <table border="0" cellpadding="0" cellspacing="0">
                                <tr>
                                    <td align="center" style="background-color: #f8fafc; border-radius: 6px; padding: 15px 40px; border: 1px solid #e2e8f0;">
                                        <h2 style="margin: 0; font-size: 36px; font-weight: 700; color: #3b82f6; letter-spacing: 8px;">{{OTP_CODE}}</h2>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>

                    <!-- Security Warning -->
                    <tr>
                        <td align="left" style="padding: 0 30px 40px 30px; color: #555555; font-size: 14px; line-height: 1.6;">
                            <p style="margin: 0 0 20px 0;">For your security, please do not share this code with anyone. If you did not request to log in, you can safely ignore this email.</p>
                            <p style="margin: 0;">Stay secure,<br><strong>The ContextGPT Team</strong></p>
                        </td>
                    </tr>
                </table>
                <!-- End Main Card -->

                <!-- Footer -->
                <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px;">
                    <tr>
                        <td align="center" style="padding: 30px 30px; color: #64748b; font-size: 12px; line-height: 1.6;">
                            <p style="margin: 0 0 10px 0;">&copy; 2026 ContextGPT. All rights reserved.</p>
                            <p style="margin: 0;">Need help? Contact us at <a href="mailto:support@ContextGPT .com" style="color: #3b82f6; text-decoration: underline;">support@ContextGPT .com</a></p>
                        </td>
                    </tr>
                </table>
                <!-- End Footer -->

            </td>
        </tr>
    </table>
</body>
</html>
"""