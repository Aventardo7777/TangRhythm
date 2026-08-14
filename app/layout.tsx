import "./globals.css";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "TangRhythm · 唐韵",
  description: "基于知识图谱、统计分析与生成式 AI 的中国古典诗词智能教学平台"
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return <html lang="zh-CN"><body>{children}</body></html>;
}
