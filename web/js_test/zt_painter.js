PainterTest = TestCase('PainterTest');

PainterTest.prototype.setUp = function (){
	paper.setup();
	paper.install(window);
	
	toolkit = [Path.Circle];
};

PainterTest.prototype.testAdd = function (){
	obj = Painter.add(0, [[100, -10], 40]);
	
	assertEquals(obj.position.x, 100);
	assertEquals(obj.position.y, -10);
};

PainterTest.prototype.testProcess = function (){
	var item1 = [0, [[100, -10], 40]];
	var item2 = [0, [[-20, -10], 20]];
	
	objects = Painter.process([item1, item2]);
	
	assertEquals(objects[0].position.x, 100);
	assertEquals(objects[0].position.y, -10);
	
	assertEquals(objects[1].position.x, -20);
	assertEquals(objects[1].position.y, -10);
};