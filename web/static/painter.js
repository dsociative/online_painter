$(document).ready(function() {
    updater.poll();
    
    var canvas = document.getElementById('myCanvas');
    var points = [];
    
    paper.install(window);
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
    		action(0, points_ident.apply(this, points));
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
		
	add: function(id, args){
		var tool = toolkit[id];
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
			var id = seq[no][0];
			var args = seq[no][1];
			
			console.log(args)
			objects.push(this.add(id, args));
			
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