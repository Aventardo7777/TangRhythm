'use client';
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, PieChart, Pie, Cell } from "recharts";

export function ThemeChart({data}:{data:{name:string,value:number}[]}) {
 return <div className="h-64 w-full"><ResponsiveContainer><BarChart data={data}><XAxis dataKey="name" tick={{fontSize:12}}/><YAxis hide/><Tooltip/><Bar dataKey="value" fill="#365d52" radius={[6,6,0,0]}/></BarChart></ResponsiveContainer></div>
}
export function EmotionChart({data}:{data:{name:string,value:number}[]}) {
 return <div className="h-64 w-full"><ResponsiveContainer><PieChart><Pie data={data} dataKey="value" nameKey="name" innerRadius={55} outerRadius={88} paddingAngle={3}>{data.map((_,i)=><Cell key={i} fill={["#365d52","#9f4638","#b28a45","#66736c","#9a765e","#485b55"][i%6]}/>)}</Pie><Tooltip/></PieChart></ResponsiveContainer></div>
}
