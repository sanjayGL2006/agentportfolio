# Scratchpad - Verify Certificates Page

## Plan
1. Open `file:///c:/Users/Sanjay%20G%20L/Desktop/portfiler/certificates.html` in the browser.
2. Verify total certificates loaded (expected: 96).
3. Test filter buttons:
    - Python
    - AI
    - Cybersecurity
    - Government
4. Open preview modal by clicking a certificate card.
5. Check if "View Certificate" button is present and linked to Google Drive.
6. Take screenshots for aesthetics.

## Progress
- [x] Open certificates page (Failed: Playwright browser context failed to initialize due to driver download error)
- [ ] Verify 96 certificates loaded
- [ ] Test filter buttons
- [ ] Open preview modal
- [ ] Verify "View Certificate" link
- [ ] Take screenshots

## Findings
The `open_browser_url` tool failed consistently with:
`failed to create browser context: failed to run playwright manager: failed to install playwright: could not install driver: could not install driver: error: got non 200 status code: 404 (404 Not Found) from https://playwright.azureedge.net/builds/driver/playwright-1.57.0-win32_x64.zip`
Additionally, direct access to `file:///` URLs is blocked by the tool's parameter constraints.
