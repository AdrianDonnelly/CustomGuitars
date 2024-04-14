import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
const fileName = urlParams.get('file_name');
console.log(fileName)


let width = window.innerWidth,
height = window.innerHeight;

let renderer = new THREE.WebGLRenderer();
renderer.setSize(width, height);
renderer.setClearColor(0x444444);
document.body.appendChild(renderer.domElement);


let scene = new THREE.Scene();



let camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 10000);
camera.position.z = 30;
scene.add(camera);

renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap;

const skycolor = 0xFFFFFF;
const skyintensity = 2;
const skylight = new THREE.AmbientLight(skycolor, skyintensity);
scene.add(skylight);

const color = 0xFFFFFF;
const intensity = 9;
const light = new THREE.DirectionalLight(color, intensity);
light.position.set(0, 10, 5);
light.target.position.set(-5, 0, 0);
scene.add(light);
scene.add(light.target);



let controls = new OrbitControls(camera, renderer.domElement);


//let axes = new THREE.AxisHelper(50);
//scene.add( axes );

const planeSize = 25;
     
const texloader = new THREE.TextureLoader();
const texture = texloader.load('/static/models/resources/31107-1814430194.jpg');
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
const referenceSize = 5;
loader.load( `/static/models/${fileName}.glb`, function ( gltf ) {
	gltf.scene.position.y = 1.5;

	const boundingBox = new THREE.Box3().setFromObject(gltf.scene);
    const center = boundingBox.getCenter(new THREE.Vector3());

	const size = new THREE.Vector3();
    boundingBox.getSize(size);
	const scaleFactor = referenceSize / Math.max(size.x, size.y, size.z);
	gltf.scene.scale.set(scaleFactor, scaleFactor, scaleFactor);
	gltf.scene.position.y = 1.5;

    // Adjust camera position and look at the center of the model
    camera.position.set(center.x, center.y, center.z + 10); // Adjust the distance from the model
    camera.lookAt(center); // Make the camera look at the center of the model

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
