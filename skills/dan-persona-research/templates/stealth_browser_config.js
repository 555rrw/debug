/**
 * Playwright Stealth 模擬配置模板
 * 用於繞過 Akamai, Cloudflare, PerimeterX 偵測
 */

const stealthConfig = {
  vendor: 'Intel Inc.',
  renderer: 'Intel(R) Iris(R) Xe Graphics',
  nav_user_agent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
  nav_platform: 'Win32',
  languages: ['en-US', 'en'],
  runOnContext: (context) => {
    // 隱藏 webdriver 標誌
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
    // 模擬 Chrome 插件環境
    window.chrome = { runtime: {} };
    // 模擬 Permissions API
    const originalQuery = window.navigator.permissions.query;
    window.navigator.permissions.query = (parameters) => (
      parameters.name === 'notifications' ?
        Promise.resolve({ state: Notification.permission }) :
        originalQuery(parameters)
    );
  }
};

module.exports = stealthConfig;
