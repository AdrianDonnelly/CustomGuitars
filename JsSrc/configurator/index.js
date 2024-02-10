import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';


let width = window.innerWidth,
height = window.innerHeight;

let renderer = new THREE.WebGLRenderer();
renderer.setSize(width, height);
renderer.setClearColor(0xEEEEEf);
document.body.appendChild(renderer.domElement);


let scene = new THREE.Scene();



let camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 10000);
camera.position.z = 30;
scene.add(camera);



const color = 0xFFFFFF;
const intensity = 4;
const light = new THREE.AmbientLight(color, intensity);
scene.add(light);

const spotLight = new THREE.SpotLight( 0xffffff );
spotLight.intensity = 10;
spotLight.position.set( 1000, 1000, 1000 );

let controls = new OrbitControls(camera, renderer.domElement);


//let axes = new THREE.AxisHelper(50);
//scene.add( axes );

const planeSize = 40;
     
const texloader = new THREE.TextureLoader();
const texture = texloader.load('/static/models/resources/checker.png');
texture.wrapS = THREE.RepeatWrapping;
texture.wrapT = THREE.RepeatWrapping;
texture.magFilter = THREE.NearestFilter;
texture.colorSpace = THREE.SRGBColorSpace;
const repeats = planeSize / 2;
texture.repeat.set(repeats, repeats);

const planeGeo = new THREE.PlaneGeometry(planeSize, planeSize);
const planeMat = new THREE.MeshPhongMaterial({
  map: texture,
  side: THREE.DoubleSide,
});
const mesh = new THREE.Mesh(planeGeo, planeMat);
mesh.rotation.x = Math.PI * -.5;
scene.add(mesh);



const loader = new GLTFLoader();
loader.load( '/static/models/truck/scene.gltf', function ( gltf ) {
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

