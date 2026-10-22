"""Refresh public GitHub metadata without credentials; no private content is read."""
import concurrent.futures,datetime,json,pathlib,urllib.request
PROJECTS = [
 {'name':'frankstop.github.io','title':'Portfolio','summary':'Independently deployed projects, brought together in one website.','feats':['12,000 canvas particles move through four mathematical vortex fields.','Lazy-loaded project previews and a live resume viewer compose separately deployed sites.'],'evidence':'README.md'},
 {'name':'KingKullenResearch','title':'King Kullen Research','summary':'A historical grocery-price pipeline and searchable item explorer.','feats':['UPC matching compares dated catalog snapshots and retains missing and returned items.','An 80% catalog-match gate prevents partial crawls from becoming the next published baseline.'],'evidence':'README.md','status':'Retired · Sep 6, 2026'},
 {'name':'OthelloAISource','title':'Othello AI','summary':'A full-stack strategy game that makes its AI reasoning visible.','feats':['Four opponents: Greedy, Minimax, Alpha-Beta Pruning and Monte Carlo Tree Search.','A real-time analysis heatmap visualizes move evaluations, backed by FastAPI and SQLite.'],'evidence':'readme.txt','language_note':'GitHub byte counts include the committed virtual environment.'}
]
def fetch(url):
 req=urllib.request.Request(url,headers={'Accept':'application/vnd.github+json','User-Agent':'Frank-Portfolio-Test'})
 with urllib.request.urlopen(req,timeout=25) as r:return json.load(r)
def enrich(p):
 base='https://api.github.com/repos/frankstop/'+p['name'];meta=fetch(base);langs=fetch(base+'/languages')
 assert meta['private'] is False
 return {**p,'url':meta['html_url'],'pushed_at':meta['pushed_at'],'languages':langs,'evidence_url':meta['html_url']+'/blob/'+meta['default_branch']+'/'+p['evidence']}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex: projects=list(ex.map(enrich,PROJECTS))
pathlib.Path('dist/projects.json').write_text(json.dumps({'fetched_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'projects':projects},indent=2)+'\n')
print('Saved metadata and language-byte counts for',len(projects),'public repositories.')
