import Link from "next/link";
import { ArrowLeft, Search } from "lucide-react";
import { poems } from "@/data/poems";

export default function PoetryPage() {
  return <main className="min-h-screen bg-[var(--paper)]">
    <div className="mx-auto max-w-6xl px-6 py-10">
      <Link href="/" className="text-sm text-[var(--muted)]">← 返回 TangRhythm</Link>
      <div className="mt-14 flex flex-col justify-between gap-6 md:flex-row md:items-end">
        <div><div className="text-xs uppercase tracking-[.25em] text-[var(--gold)]">Poetry Explorer</div><h1 className="serif mt-2 text-5xl font-black">唐诗</h1><p className="mt-3 text-[var(--muted)]">从一首诗开始，进入一个时代。</p></div>
        <div className="flex items-center gap-2 rounded-full border border-[var(--line)] bg-white/60 px-4 py-3 text-sm text-[var(--muted)]"><Search size={16}/> 搜索诗名、作者、主题……</div>
      </div>
      <div className="mt-12 grid gap-4 md:grid-cols-2">
        {poems.map(p => <Link key={p.id} href={`/poetry/${p.id}`} className="group rounded-3xl border border-[var(--line)] bg-white/50 p-7 transition hover:-translate-y-1 hover:bg-white">
          <div className="flex items-start justify-between"><div><div className="text-xs text-[var(--muted)]">{p.dynasty} · {p.author}</div><h2 className="serif mt-2 text-2xl font-bold">{p.title}</h2></div><span className="rounded-full bg-[var(--jade-soft)] px-3 py-1 text-xs text-[var(--jade)]">{p.theme}</span></div>
          <p className="serif mt-7 whitespace-pre-line text-lg leading-9">{p.content}</p>
          <div className="mt-6 text-xs text-[var(--muted)] group-hover:text-[var(--jade)]">进入诗笺 →</div>
        </Link>)}
      </div>
    </div>
  </main>;
}
