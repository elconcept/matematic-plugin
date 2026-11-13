import pathlib,json,re,sys
p=pathlib.Path(sys.argv[1] if len(sys.argv)>1 else '.')
m=json.loads((p/'plugin.json').read_text(encoding='utf-8'))
assert m['name']=='matematic-plugin' and m['$schema']=='https://agent-plugins.org/schemas/1.0.0/plugin.schema.json'
assert len(m['extensions']['com.openai']['interface']['shortDescription'])<=30
skills=list((p/'skills').glob('*/SKILL.md'))
assert len(skills)==33,len(skills)
for s in skills:
 t=s.read_text(encoding='utf-8')
 assert t.startswith('---\n') and '\n---\n' in t[4:],s
 assert re.search(r'^name: '+re.escape(s.parent.name)+r'$',t,re.M),s
 assert re.search(r'^description: ',t,re.M),s
 assert (s.parent/'LICENSE').exists(),s
 a=(s.parent/'agents/openai.yaml').read_text(encoding='utf-8')
 assert 'products: [CHAT]' in a and 'allow_implicit_invocation: true' in a,s
assert not any(x.name.lower() in ('mcp.json','.mcp.json','.app.json') for x in p.rglob('*'))
print('PASS 33 skills, 33 policies CHAT, licenses, zero transport manifests')
