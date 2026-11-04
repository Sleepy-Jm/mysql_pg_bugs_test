(async()=>{
const fs=await import('node:fs/promises');
function calculate(spec) {
 const rows=[], details=[];
 for(const [ps,values] of Object.entries(spec.data)) {
  const p=Number(ps),n=values.length;
  for(let i=1;i<=n;i++) {
   const l=spec.lo==="unbounded"?1:spec.lo==="preceding"?Math.max(1,i-2):spec.lo==="following"?i+2:i;
   const u=spec.hi==="unbounded"?n:spec.hi==="following"?Math.min(n,i+3):i;
   const ids=[];let s=0,k=0;
   for(let j=l;j<=u;j++){ids.push(j);if(values[j-1]!==null){s+=values[j-1];k++;}}
   let v=null;
   if(k){if(spec.real)v=s/k;else {const q=(BigInt(s)*2000000n+BigInt(k))/(2n*BigInt(k));v=(q/1000000n).toString()+"."+(q%1000000n).toString().padStart(6,"0");}}
   rows.push([p,i,v]);details.push([spec.case_id,p,i,ids.join(",")||"empty",s,k,k?s+"/"+k:"NULL",v===null?"NULL":v]);
  }
 }
 return {rows,details};
}
const specs=[{"case_id":"WF_BASE","lo":"preceding","hi":"following","data":{"1":[60,180,120,300,240,420,360,540,480]},"real":false},{"case_id":"WF_CURRENT","lo":"preceding","hi":"current","data":{"1":[60,180,120,300,240,420,360,540,480],"2":[120,300],"3":[240]},"real":false},{"case_id":"WF_UNBOUNDED","lo":"preceding","hi":"unbounded","data":{"1":[60,180,120,300,240,420,360,540,480],"2":[120,300],"3":[240]},"real":false},{"case_id":"WF_CUMULATIVE","lo":"unbounded","hi":"current","data":{"1":[60,180,120,300,240,420,360,540,480],"2":[120,300],"3":[240]},"real":false},{"case_id":"WF_NULLS","lo":"preceding","hi":"following","data":{"1":[60,null,120,300,null,420,360,null,480],"2":[120,300],"3":[240],"4":[null,null,null]},"real":false},{"case_id":"WF_EMPTY","lo":"following","hi":"following","data":{"1":[60,null,120,300,null,420,360,null,480],"2":[120,300],"3":[240],"4":[null,null,null]},"real":false},{"case_id":"WF_REAL_LOW","lo":"preceding","hi":"following","data":{"1":[60,null,120,300,null,420,360,null,480],"2":[120,300],"3":[240],"4":[null,null,null]},"real":true},{"case_id":"WF_REAL_HIGH","lo":"preceding","hi":"following","data":{"1":[60,null,120,300,null,420,360,null,480],"2":[120,300],"3":[240],"4":[null,null,null]},"real":true}];
const expected=JSON.parse(await fs.readFile(new URL('./expected.json',import.meta.url),'utf8'));
for(const spec of specs){const c=expected.cases.find(c=>c.case_id===spec.case_id);if(JSON.stringify(c.rows)!==JSON.stringify(calculate(spec).rows))throw Error(spec.case_id);}
console.log('Pure arithmetic oracle check: '+specs.length+' cases; no database execution.');
})()