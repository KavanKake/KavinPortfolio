// Genererer /sitemap.xml ved build. Legg nye sider til i listen under.
import { links } from "$lib/data/profile.js";

export const prerender = true;

const pages = [
  { path: "/", priority: "1.0", changefreq: "weekly" },
  { path: "/projects", priority: "0.9", changefreq: "weekly" },
  { path: "/aboutme", priority: "0.8", changefreq: "monthly" },
  { path: "/contactme", priority: "0.7", changefreq: "yearly" },
  { path: "/privacy", priority: "0.3", changefreq: "yearly" }
];

export function GET() {
  const lastmod = new Date().toISOString().slice(0, 10);
  const urls = pages
    .map(
      (p) => `  <url>
    <loc>${links.site}${p.path}</loc>
    <lastmod>${lastmod}</lastmod>
    <changefreq>${p.changefreq}</changefreq>
    <priority>${p.priority}</priority>
  </url>`
    )
    .join("\n");

  const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${urls}
</urlset>
`;
  return new Response(xml, { headers: { "Content-Type": "application/xml" } });
}
