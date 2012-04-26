paper.install(window);

var tool_id = 0
var points = [];

$(document).ready(function() {
    updater.poll();
    
    var canvas = document.getElementById('myCanvas');
    
    paper.setup(canvas);

    project.currentStyle = {
    	    strokeColor: 'black',
    	    fillColor:'red',
    };
    
    toolkit = [Path.Circle];
    
    tool = new Tool();
    
    load_action();
    
    tool.onMouseDown = function (event){
    	var point = event.point.round(); 
    	points.push(point);
    };
    
    tool.onMouseUp = function (event){
    	var point = event.point.round();
    	points.push(point);
    	
    	if (points.length == 2){
    		action(tool_id, points_ident.apply(this, points));
    		points = [];
    	};
    };

});

function points_ident(){
	var seq = []
	
	for (var i in arguments){
		seq.push([arguments[i].x, arguments[i].y])
	}
	console.log(arguments)
	console.log(seq)
	
	return seq;
};

function load_action(){
    $.get('/pooling', function(data){
    	process(data);
    })
};

function action(id, args){
	$.post('/action', {id: id, args: JSON.stringify(args)});
};

var updater = {
    errorSleepTime: 500,
    cursor: null,

    poll: function() {
        var args = {"_xsrf": 0};
        if (updater.cursor) args.cursor = updater.cursor;
        $.ajax({url: "/pooling", type: "POST", dataType: "text",
                data: $.param(args), success: updater.onSuccess,
                error: updater.onError});
    },

    onSuccess: function(response) {
        try {
            process(response);
        } catch (e) {
            updater.onError();
            return;
        }
        updater.errorSleepTime = 500;
        window.setTimeout(updater.poll, 0);
    },

    onError: function(response) {
        updater.errorSleepTime *= 2;
        console.log("Poll error; sleeping for", updater.errorSleepTime, "ms");
        window.setTimeout(updater.poll, updater.errorSleepTime);
    },

};

var Painter = {
		
	toolkit: [Path.Circle, Path.Line],
		
	add: function(id, args){
		var tool = this.toolkit[id];
		return tool.apply(this, args);
	},
	
	clear: function(){
	    project.activeLayer.remove();
	    var layer = new Layer();
	},
	
	process: function(seq){
		this.clear();
		var objects = [];
		
		for (var no in seq){
			objects.push(this.add(seq[no][0], seq[no][1]));
		}
		
		if (view){
			view.draw();
		}
		
		return objects;
	}
	
}

function process(response){
	var data = JSON.parse(response)
	Painter.process(data);
}