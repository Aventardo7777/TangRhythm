import Link from "next/link";
import { ArrowUpRight, BookOpen, Compass, Feather, Map, Sparkles, TrendingUp } from "lucide-react";
import { poems, stats, themes, imagery } from "@/data/poems";
import { ThemeChart, EmotionChart } from "@/components/Charts";

export default function Home() {
  return (
    <main className="min-h-screen paper-grid">
      <nav className="mx-auto flex max-w-7xl items-center justify-between px-6 py-6">
        <div className="flex items-center gap-3">
          <div className="grid h-10 w-10 place-items-center rounded-full bg-[var(--jade)] text-[var(--paper)]"><Feather size={19}/></div>
          <div><div className="serif text-lg font-bold">TangRhythm</div><div className="text-[10px] uppercase tracking-[.28em] text-[var(--muted)]">唐韵 · Digital Humanities</div></div>
        </div>
        <div className="hidden gap-7 text-sm text-[var(--muted)] md:flex">
          <Link href="/poetry" className="hover:text-[var(--ink)]">诗歌</Link>
          <a href="#explore" className="hover:text-[var(--ink)]">探索</a>
          <a href="#ai" className="hover:text-[var(--ink)]">AI 老师</a>
          <a href="#learning" className="hover:text-[var(--ink)]">学习</a>
        </div>
        <Link href="/poetry" className="rounded-full border border-[var(--line)] bg-white/50 px-4 py-2 text-sm">开始探索 →</Link>
      </nav>

      <section className="mx-auto max-w-7xl px-6 pb-20 pt-14 md:pt-24">
        <div className="max-w-4xl">
          <div className="mb-7 flex items-center gap-3 text-xs uppercase tracking-[.3em] text-[var(--vermilion)]"><span className="h-px w-10 bg-[var(--vermilion)]"/>Tang Poetry · AI · Data</div>
          <h1 className="serif text-5xl font-black leading-[1.15] md:text-7xl">一卷唐诗，<br/><span className="text-[var(--jade)]">读见千年风华。</span></h1>
          <p className="mt-7 max-w-2xl text-lg leading-9 text-[var(--muted)]">把三百首唐诗从静态文本变成可以搜索、理解、分析、探索与学习的数字知识宇宙。</p>
          <div className="mt-9 flex flex-wrap gap-3">
            <Link href="/poetry" className="inline-flex items-center gap-2 rounded-full bg-[var(--jade)] px-6 py-3 text-sm font-semibold text-white shadow-lg shadow-black/10">探索唐诗 <ArrowUpRight size={16}/></Link>
            <a href="#explore" className="rounded-full border border-[var(--line)] bg-white/50 px-6 py-3 text-sm">看看数据如何说话</a>
          </div>
        </div>

        <div className="mt-20 grid grid-cols-2 gap-3 md:grid-cols-4">
          {[
            [stats.poems, "首诗歌"], [stats.authors, "位诗人"], [stats.themes, "个主题"], [stats.relations, "语义关系"]
          ].map(([n,l]) => <div key={l} className="rounded-2xl border border-[var(--line)] bg-white/45 p-5"><div className="serif text-3xl font-bold">{n}</div><div className="mt-1 text-xs text-[var(--muted)]">{l}</div></div>)}
        </div>
      </section>

      <section id="explore" className="border-y border-[var(--line)] bg-white/35">
        <div className="mx-auto max-w-7xl px-6 py-20">
          <div className="mb-10 flex items-end justify-between"><div><div className="text-xs uppercase tracking-[.25em] text-[var(--gold)]">Explore the corpus</div><h2 className="serif mt-2 text-3xl font-bold">让数据讲一遍唐诗</h2></div><Compass className="text-[var(--jade)]"/></div>
          <div className="grid gap-5 lg:grid-cols-2">
            <div className="rounded-3xl border border-[var(--line)] bg-[var(--paper)] p-6"><div className="mb-5 flex items-center gap-2"><TrendingUp size={17}/><span className="font-semibold">主题分布</span></div><ThemeChart data={themes}/></div>
            <div className="rounded-3xl border border-[var(--line)] bg-[var(--paper)] p-6"><div className="mb-5 flex items-center gap-2"><Sparkles size={17}/><span className="font-semibold">情绪画像</span></div><EmotionChart data={stats.emotions}/></div>
          </div>
          <div className="mt-5 grid gap-5 md:grid-cols-3">
            {[
              ["唐诗地图", "从长安到江南，诗歌沿着真实的中国地理空间流动。", Map],
              ["意象网络", "月、酒、山、水、雁、舟……看见诗歌背后的共同语言。", Compass],
              ["AI 老师", "从小学到高中，用不同深度重新解释同一首诗。", Sparkles]
            ].map(([title, desc, Icon]) => <div key={String(title)} className="rounded-3xl border border-[var(--line)] bg-[var(--paper)] p-7"><Icon className="mb-8 text-[var(--jade)]"/><h3 className="serif text-xl font-bold">{String(title)}</h3><p className="mt-3 text-sm leading-7 text-[var(--muted)]">{String(desc)}</p></div>)}
          </div>
        </div>
      </section>

      <section id="ai" className="mx-auto max-w-7xl px-6 py-20">
        <div className="grid gap-12 lg:grid-cols-[1fr_1.2fr] lg:items-center">
          <div><div className="text-xs uppercase tracking-[.25em] text-[var(--vermilion)]">TangRhythm AI Teacher</div><h2 className="serif mt-3 text-4xl font-bold">不只是解释，<br/>而是教你理解。</h2><p className="mt-6 leading-8 text-[var(--muted)]">AI 教师通过知识检索、诗歌上下文、作者资料与历史背景组织回答，再根据学习者年龄与目的调整语言。</p><div className="mt-7 flex flex-wrap gap-2">{["小学模式","初中模式","高中模式","深度模式","教师模式"].map(x=><span key={x} className="rounded-full bg-[var(--jade-soft)] px-3 py-1.5 text-xs text-[var(--jade)]">{x}</span>)}</div></div>
          <div className="rounded-[2rem] border border-[var(--line)] bg-[#1f2421] p-7 text-[#f7f3ea] shadow-2xl">
            <div className="mb-8 flex items-center gap-3 text-sm"><div className="grid h-9 w-9 place-items-center rounded-full bg-[#365d52]"><Sparkles size={15}/></div>TangRhythm AI Teacher</div>
            <div className="space-y-5 text-sm leading-7"><div className="ml-auto max-w-[82%] rounded-2xl rounded-tr-sm bg-white/10 p-4">为什么“感时花溅泪”会把花写得像人在流泪？</div><div className="max-w-[90%] rounded-2xl rounded-tl-sm bg-[#f7f3ea] p-5 text-[#1f2421]">这里不只是“拟人”。杜甫把自己的悲痛投射到眼前的花鸟之中，花本来不会流泪，但诗人看到花时的心境，使花也仿佛带上了人的悲哀。这种“移情”让景物与人的情感融在一起。</div></div>
          </div>
        </div>
      </section>

      <section id="learning" className="border-t border-[var(--line)] bg-[#e9e4d8]">
        <div className="mx-auto max-w-7xl px-6 py-20">
          <div className="grid gap-10 md:grid-cols-3">
            <div><BookOpen className="text-[var(--jade)]"/><h3 className="serif mt-4 text-2xl font-bold">阅读</h3><p className="mt-3 text-sm leading-7 text-[var(--muted)]">逐句解释、竖排阅读、名句收藏与作者探索。</p></div>
            <div><TrendingUp className="text-[var(--jade)]"/><h3 className="serif mt-4 text-2xl font-bold">掌握</h3><p className="mt-3 text-sm leading-7 text-[var(--muted)]">背诵、填空、测试、错题与间隔复习。</p></div>
            <div><Sparkles className="text-[var(--jade)]"/><h3 className="serif mt-4 text-2xl font-bold">成长</h3><p className="mt-3 text-sm leading-7 text-[var(--muted)]">通过 Mastery Score 观察自己的学习轨迹。</p></div>
          </div>
        </div>
      </section>

      <footer className="mx-auto max-w-7xl px-6 py-10 text-xs text-[var(--muted)]">TangRhythm · Digital Humanities · 让古诗词不只是被背下来，而是被真正理解。</footer>
    </main>
  );
}
