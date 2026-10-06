import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({ subsets: ["latin"], variable: "--font-sans" });

export const metadata: Metadata = {
  title: "Sanjay G L | Personal SEO & Digital Identity Analyzer",
  description: "Analyze and improve your digital identity and SEO presence across the web.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className="dark">
      <body
        className={`${inter.variable} font-sans antialiased bg-background text-foreground min-h-screen`}
      >
        <div className="flex h-screen overflow-hidden">
          {children}
        </div>
      </body>
    </html>
  );
}
