/** @type {import('next-sitemap').IConfig} */
module.exports = {
  siteUrl: '[WEB_SITE]',
  generateRobotsTxt: true,
  generateIndexSitemap: false,
  robotsTxtOptions: {
    policies: [{ userAgent: '*', allow: '/' }],
    additionalSitemaps: [
      '[WEB_SITE]/sitemap.xml',
      '[WEB_SITE]/server-sitemap.xml',
    ],
  },
};
