LOGIN = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>New Login Alert - ContextGPT</title>
    <style>
        /* Reset styles */
        body, table, td, a { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; }
        table, td { mso-table-lspace: 0pt; mso-table-rspace: 0pt; }
        img { -ms-interpolation-mode: bicubic; }
        img { border: 0; height: auto; line-height: 100%; outline: none; text-decoration: none; }
        table { border-collapse: collapse !important; }
        body { height: 100% !important; margin: 0 !important; padding: 0 !important; width: 100% !important; }
        a[x-apple-data-detectors] { color: inherit !important; text-decoration: none !important; font-size: inherit !important; font-family: inherit !important; font-weight: inherit !important; line-height: inherit !important; }
    </style>
</head>
<!-- Outer background updated to a sleek, modern tech gray -->
<body style="background-color: #f3f4f6; margin: 0 !important; padding: 0 !important; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;">

    <!-- Wrapper Table -->
    <table border="0" cellpadding="0" cellspacing="0" width="100%">
        <tr>
            <td align="center" style="padding: 40px 10px 40px 10px;">
                
                <!-- Main Container -->
                <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px; background-color: #ffffff; border-radius: 8px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);">
                    
                    <!-- Header (Dark tech-focused background) -->
                    <tr>
                        <td align="center" style="padding: 30px 30px 20px 30px; background-color: #0f172a; border-top-left-radius: 8px; border-top-right-radius: 8px;">
                            <h1 style="margin: 0; color: #ffffff; font-size: 24px; font-weight: 700; letter-spacing: 2px;">ContextGPT</h1>
                        </td>
                    </tr>

                    <!-- Body Content -->
                    <tr>
                        <td align="left" style="padding: 40px 30px 20px 30px; color: #333333; font-size: 16px; line-height: 1.6;">
                            <h2 style="margin: 0 0 20px 0; color: #0f172a; font-size: 20px; font-weight: 600;">New sign-in detected</h2>
                            <p style="margin: 0 0 20px 0;">Hi <strong>{{USER_NAME}}</strong>,</p>
                            <p style="margin: 0 0 20px 0;">We noticed a new sign-in to your ContextGPT account from an IP Address we don't recognize. Here are the details:</p>
                        </td>
                    </tr>

                    <!-- Details Box (Light Blue/Crypto Theme) -->
                    <tr>
                        <td align="center" style="padding: 0 30px 30px 30px;">
                            <table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color: #f8fafc; border-radius: 6px; border: 1px solid #e2e8f0;">
                                <tr>
                                    <td align="left" style="padding: 20px; color: #333333; font-size: 14px; line-height: 1.8;">
                                       <strong>Time:</strong> {{LOGIN_TIME}}<br>
                                        <strong>IP Address:</strong> {{IP_ADDRESS}}
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>

                    <!-- Action Steps -->
                    <tr>
                        <td align="left" style="padding: 0 30px 20px 30px; color: #333333; font-size: 16px; line-height: 1.6;">
                            <p style="margin: 0 0 20px 0;"><strong>Was this you?</strong><br>
                            If you recognize this activity, you are all set and can safely ignore this email.</p>
                            
                            <p style="margin: 0 0 10px 0;"><strong>Wasn't you?</strong><br>
                            If you did not sign in recently, someone else may have access to your account. Please secure your account immediately by following these steps:</p>
                        </td>
                    </tr>

                    <!-- Security Instructions -->
                    <tr>
                        <td align="left" style="padding: 0 30px 40px 30px; color: #555555; font-size: 15px; line-height: 1.6;">
                            <ol style="margin: 0; padding-left: 20px; background-color: #f8fafc; border-radius: 6px; border: 1px solid #e2e8f0; padding: 20px 20px 20px 40px;">
                                <li style="margin-bottom: 10px;">Go to the <strong>Profile</strong> section in your dashboard.</li>
                                <li style="margin-bottom: 10px;">Click on the <strong>Security</strong> settings.</li>
                                <li style="margin-bottom: 0;">Select <strong>Change Password</strong> to update your credentials immediately.</li>
                            </ol>
                        </td>
                    </tr>
                    
                    <!-- Sign-off -->
                    <tr>
                        <td align="left" style="padding: 0 30px 40px 30px; color: #555555; font-size: 14px; line-height: 1.6;">
                            <p style="margin: 0;">Stay secure,<br><strong>The ContextGPT Team</strong></p>
                        </td>
                    </tr>
                </table>
                <!-- End Main Container -->

                <!-- Footer -->
                <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px;">
                    <tr>
                        <td align="center" style="padding: 30px 30px; color: #64748b; font-size: 12px; line-height: 1.6;">
                            <p style="margin: 0 0 10px 0;">This is an automated security alert. Please do not reply to this email.</p>
                            <p style="margin: 0 0 10px 0;">&copy; 2026 ContextGPT. All rights reserved.</p>
                            <p style="margin: 0;">
                                <a href="mailto:support@ContextGPT.com" style="color: #3b82f6; text-decoration: underline;">Contact Support</a> | 
                                <a href="{{PRIVACY_URL}}" style="color: #3b82f6; text-decoration: underline;">Privacy Policy</a>
                            </p>
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