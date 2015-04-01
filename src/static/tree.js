var store = Ext.create('Ext.data.TreeStore', {
	proxy: {
		type: 'ajax',
		url: 'treeData.json'
	},
	root: {
		text: 'Countries',
		expanded: true
	}
});

Ext.create('Ext.tree.Panel', {
	title: 'Countries &amp; Cities',
	width: 500,
	height: 300,
	store: store,
	rootVisible: false,
	renderTo: Ext.getBody(),
	style: 'margin: 50px'
});
