import os
import shutil
import re

SRC_PORTFOLIO = '/Users/supratim/Desktop/my_portfolio'
DEST_LANDING = '/Users/supratim/Desktop/flockML-landing'

os.makedirs(DEST_LANDING, exist_ok=True)

# 1. Base configs to copy
base_files = [
    'package.json',
    'tsconfig.json',
    'next.config.ts',
    'postcss.config.mjs',
    '.gitignore'
]

for bf in base_files:
    src_file = os.path.join(SRC_PORTFOLIO, bf)
    if os.path.exists(src_file):
        shutil.copy2(src_file, os.path.join(DEST_LANDING, bf))

# 2. Setup directory structure
dirs_to_make = [
    'app',
    'app/docs',
    'app/docs/[slug]',
    'app/math',
    'components',
    'components/mdx',
    'components/live',
    'content',
    'content/flockml',
    'lib',
    'lib/federated',
    'public'
]

for d in dirs_to_make:
    os.makedirs(os.path.join(DEST_LANDING, d), exist_ok=True)

# 3. Copy content/flockml
src_content = os.path.join(SRC_PORTFOLIO, 'content', 'flockml')
dest_content = os.path.join(DEST_LANDING, 'content', 'flockml')
if os.path.exists(src_content):
    for f in os.listdir(src_content):
        shutil.copy2(os.path.join(src_content, f), os.path.join(dest_content, f))

# 4. Copy public assets
src_public = os.path.join(SRC_PORTFOLIO, 'public')
dest_public = os.path.join(DEST_LANDING, 'public')
if os.path.exists(src_public):
    for f in os.listdir(src_public):
        src_p = os.path.join(src_public, f)
        dest_p = os.path.join(dest_public, f)
        if os.path.isfile(src_p):
            shutil.copy2(src_p, dest_p)
        elif os.path.isdir(src_p):
            shutil.copytree(src_p, dest_p, dirs_exist_ok=True)

# 5. Copy lib/docs.ts and lib/federated
src_lib_docs = os.path.join(SRC_PORTFOLIO, 'lib', 'docs.ts')
dest_lib_docs = os.path.join(DEST_LANDING, 'lib', 'docs.ts')
if os.path.exists(src_lib_docs):
    shutil.copy2(src_lib_docs, dest_lib_docs)

src_lib_fed = os.path.join(SRC_PORTFOLIO, 'lib', 'federated')
dest_lib_fed = os.path.join(DEST_LANDING, 'lib', 'federated')
if os.path.exists(src_lib_fed):
    shutil.copytree(src_lib_fed, dest_lib_fed, dirs_exist_ok=True)

# 6. Copy components
comps = [
    'FlockNavbar.tsx',
    'FlockEdgeNode.tsx',
    'GlowingCard.tsx',
    'SmoothScroll.tsx',
    'CustomCursor.tsx',
    'WarpingGrid.tsx'
]

for c in comps:
    src_c = os.path.join(SRC_PORTFOLIO, 'components', c)
    if os.path.exists(src_c):
        shutil.copy2(src_c, os.path.join(DEST_LANDING, 'components', c))

# Copy components/mdx and components/live
for sub in ['mdx', 'live']:
    s_dir = os.path.join(SRC_PORTFOLIO, 'components', sub)
    d_dir = os.path.join(DEST_LANDING, 'components', sub)
    if os.path.exists(s_dir):
        shutil.copytree(s_dir, d_dir, dirs_exist_ok=True)

# 7. Copy and adapt app files
# globals.css
src_globals = os.path.join(SRC_PORTFOLIO, 'app', 'globals.css')
dest_globals = os.path.join(DEST_LANDING, 'app', 'globals.css')
if os.path.exists(src_globals):
    shutil.copy2(src_globals, dest_globals)

# app/flock-ml/page.tsx -> app/page.tsx (root landing)
src_landing = os.path.join(SRC_PORTFOLIO, 'app', 'flock-ml', 'page.tsx')
dest_landing = os.path.join(DEST_LANDING, 'app', 'page.tsx')
if os.path.exists(src_landing):
    with open(src_landing, 'r', encoding='utf-8') as f:
        code = f.read()
    # Replace /flock-ml/docs -> /docs, /flock-ml/math -> /math, /flock-ml -> /
    code = code.replace("'/flock-ml/docs'", "'/docs'").replace('"/flock-ml/docs"', '"/docs"')
    code = code.replace("'/flock-ml/math'", "'/math'").replace('"/flock-ml/math"', '"/math"')
    code = code.replace("'/flock-ml'", "'/'").replace('"/flock-ml"', '"/"')
    with open(dest_landing, 'w', encoding='utf-8') as f:
        f.write(code)

# app/flock-ml/docs -> app/docs
src_docs_dir = os.path.join(SRC_PORTFOLIO, 'app', 'flock-ml', 'docs')
if os.path.exists(src_docs_dir):
    for f in os.listdir(src_docs_dir):
        src_f = os.path.join(src_docs_dir, f)
        dest_f = os.path.join(DEST_LANDING, 'app', 'docs', f)
        if os.path.isfile(src_f):
            with open(src_f, 'r', encoding='utf-8') as rf:
                c = rf.read()
            c = c.replace('/flock-ml/docs', '/docs').replace('/flock-ml/math', '/math').replace('/flock-ml', '/')
            with open(dest_f, 'w', encoding='utf-8') as wf:
                wf.write(c)

# [slug]/page.tsx
src_slug = os.path.join(src_docs_dir, '[slug]', 'page.tsx')
dest_slug = os.path.join(DEST_LANDING, 'app', 'docs', '[slug]', 'page.tsx')
if os.path.exists(src_slug):
    with open(src_slug, 'r', encoding='utf-8') as rf:
        c = rf.read()
    c = c.replace('/flock-ml/docs', '/docs').replace('/flock-ml/math', '/math').replace('/flock-ml', '/')
    with open(dest_slug, 'w', encoding='utf-8') as wf:
        wf.write(c)

# app/flock-ml/math/page.tsx -> app/math/page.tsx
src_math = os.path.join(SRC_PORTFOLIO, 'app', 'flock-ml', 'math', 'page.tsx')
dest_math = os.path.join(DEST_LANDING, 'app', 'math', 'page.tsx')
if os.path.exists(src_math):
    with open(src_math, 'r', encoding='utf-8') as rf:
        c = rf.read()
    c = c.replace('/flock-ml/docs', '/docs').replace('/flock-ml/math', '/math').replace('/flock-ml', '/')
    with open(dest_math, 'w', encoding='utf-8') as wf:
        wf.write(c)

# Update FlockNavbar.tsx
navbar_path = os.path.join(DEST_LANDING, 'components', 'FlockNavbar.tsx')
if os.path.exists(navbar_path):
    with open(navbar_path, 'r', encoding='utf-8') as rf:
        c = rf.read()
    c = c.replace("pathname === '/flock-ml'", "pathname === '/'")
    c = c.replace("href=\"/flock-ml\"", "href=\"/\"")
    c = c.replace("href=\"/flock-ml/docs\"", "href=\"/docs\"")
    c = c.replace("href=\"/flock-ml/docs#flocknode\"", "href=\"/docs#flocknode\"")
    c = c.replace("href=\"/flock-ml/math\"", "href=\"/math\"")
    with open(navbar_path, 'w', encoding='utf-8') as wf:
        wf.write(c)

# Create clean root app/layout.tsx
layout_code = """import type { Metadata } from "next";
import { Inter, JetBrains_Mono } from "next/font/google";
import "./globals.css";

const inter = Inter({
  variable: "--font-inter",
  subsets: ["latin"],
});

const jetbrainsMono = JetBrains_Mono({
  variable: "--font-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "FlockML - Sovereign WebGPU AI Compute Grid",
  description: "A zero-install WebGPU and WebAssembly execution engine turning edge and enterprise hardware into a Sovereign AI Inference & Compute Grid.",
  metadataBase: new URL("https://flockml.qd.je"),
  openGraph: {
    title: "FlockML - Sovereign WebGPU AI Compute Grid",
    description: "Executing 70B & 405B LLM workloads at 70% lower cost than hyperscale clouds.",
    url: "https://flockml.qd.je",
    siteName: "FlockML",
    images: [{ url: "/opengraph-image.png", width: 1200, height: 630 }],
    locale: "en_US",
    type: "website",
  },
  twitter: {
    card: "summary_large_image",
    title: "FlockML - Sovereign WebGPU AI Compute Grid",
    description: "Executing 70B & 405B LLM workloads at 70% lower cost than hyperscale clouds.",
    images: ["/opengraph-image.png"],
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className="dark scroll-smooth">
      <body className={`${inter.variable} ${jetbrainsMono.variable} font-sans bg-[#050505] text-[#ededed] antialiased selection:bg-white selection:text-black min-h-screen`}>
        {children}
      </body>
    </html>
  );
}
"""

with open(os.path.join(DEST_LANDING, 'app', 'layout.tsx'), 'w', encoding='utf-8') as f:
    f.write(layout_code)

print("SUCCESS: Migrated FlockML landing page to /Users/supratim/Desktop/flockML-landing")
