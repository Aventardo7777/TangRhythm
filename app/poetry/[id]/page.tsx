import Link from "next/link";
import { notFound } from "next/navigation";
import { poems } from "@/data/poems";

export default async function PoemDetail({ params }: { params: Promise<{id:string}> }) {
  const { id } = await params;
  const poem = poems.find(p => p.id === id);
  if (!poem) return notFound();
  return <main className="min-h-screen bg-[var(--paper)]">
    <div className="mx-auto max-w-6xl px-6 py-10">
      <Link href="/poetry" className="text-sm text-[var(--muted)]">← 返回诗歌</Link>
      <div className="mt-12 grid gap-12 lg:grid-cols-[1.1fr_.9fr]">
        <article className="rounded-[2rem] border border-[var(--line)] bg-[#fbf8f0] p-8 md:p-12">
          <div className="text-xs uppercase tracking-[.25em] text-[var(--gold)]">{poem.dynasty} · {poem.genre}</div>
          <h1 className="serif mt-4 text-5xl font-black">{poem.title}</h1>
          <div className="mt-2 text-[var(--muted)]">{poem.author}</div>
          <div className="serif mt-12 whitespace-pre-line text-2xl leading-[2.1]">{poem.content}</div>
          <div className="mt-12 border-t border-[var(--line)] pt-8"><h2 className="serif text-xl font-bold">现代译意</h2><p className="mt-4 leading-8 text-[var(--muted)]">{poem.translation}</p></div>
        </article>
        <aside className="space-y-5">
          <section className="rounded-3xl border border-[var(--line)] bg-white/50 p-7"><div className="text-xs text-[var(--muted)]">作者</div><h2 className="serif mt-2 text-2xl font-bold">{poem.author}</h2><p className="mt-3 leading-7 text-sm text-[var(--muted)]">{poem.authorBio}</p></section>
          <section className="rounded-3xl border border-[var(--line)] bg-white/50 p-7"><div className="text-xs text-[var(--muted)]">核心知识</div><div className="mt-4 flex flex-wrap gap-2">{poem.imagery.map(x=><span key={x} className="rounded-full bg-[var(--jade-soft)] px-3 py-1.5 text-xs text-[var(--jade)]">#{x}</span>)}{poem.devices.map(x=><span key={x} className="rounded-full bg-[#efe4d8] px-3 py-1.5 text-xs text-[#87533d]">#{x}</span>)}</div></section>
          <section className="rounded-3xl bg-[var(--jade)] p-7 text-white"><div className="text-xs uppercase tracking-[.2em] text-white/60">AI Teacher</div><p className="serif mt-3 text-xl leading-8">“{poem.aiHint}”</p><button className="mt-6 rounded-full bg-white px-5 py-2 text-sm font-semibold text-[var(--jade)]">向 AI 老师提问</button></section>
        </aside>
      </div>
    </div>
  </main>;
}
