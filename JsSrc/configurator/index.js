import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';




let width = window.innerWidth,
height = window.innerHeight;

let renderer = new THREE.WebGLRenderer();
renderer.setSize(width, height);
renderer.setClearColor(0xEEEEEE);
document.body.appendChild(renderer.domElement);


let scene = new THREE.Scene();



let camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 10000);
camera.position.z = 50;
scene.add(camera);



let light = new THREE.PointLight(0xffffff);
light.position.set(-100,200,100);
scene.add(light);



let controls = new OrbitControls(camera, renderer.domElement);


//let axes = new THREE.AxisHelper(50);
//scene.add( axes );



const loader = new GLTFLoader();
loader.load( '/static/models/guitar/40Th_Telecaster_Gold_Main(1).glb', function ( gltf ) {
	scene.add( gltf.scene );

}, 
	undefined, function ( error ) {
	console.error( error );
} );



resize();
animate();

window.addEventListener('resize',resize);
function resize(){
	let w = window.innerWidth;
	let h = window.innerHeight;
	renderer.setSize(w,h);
	camera.aspect = w / h;
	camera.updateProjectionMatrix();
}

function animate() {
	renderer.render( scene, camera );
	controls.update();
requestAnimationFrame( animate );
}

//imports
import { a, password as sec } from "./ui/main";

a()

let testsdf = `object ${sec} is na`

