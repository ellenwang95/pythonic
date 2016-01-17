//for ACE editor 
var editor = ace.edit("editor");
editor.setTheme("ace/theme/monokai");
editor.session.setMode("ace/mode/python");

//on Ctrl-S, show response 
editor.commands.addCommand({
    name: 'save',
    bindKey: {win: 'Ctrl-S',  mac: 'Command-S'},
    exec: function(editor) {
    	document.getElementById('response').innerHTML = "YOU SAVED";
    	var content = editor.getValue();
    	console.log(content);
    },
    readOnly: true // false if this command should not apply in readOnly mode
});



// //listen for changes
// editor.getSession().on('change', function(e) {
// 	console.log(e);
// });

