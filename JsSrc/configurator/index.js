import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
const fileName = urlParams.get('file_name');
console.log(fileName)


let width = window.innerWidth,
height = window.innerHeight;

let renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setPixelRatio( window.devicePixelRatio );
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap;
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
const skyintensity = 3;
const skylight = new THREE.AmbientLight(skycolor, skyintensity);
scene.add(skylight);

const color = 0xFFFFFF;
const intensity = 9;
const light = new THREE.DirectionalLight(color, intensity);
if (fileName === "gibson_firebird_v_electric_guitar") {
	light.position.set(-15, 10, 5);
}
else if (fileName === "gibson_sg_guitar"){
	light.position.set(0, 3, 5);
}else{
	light.position.set(0, 3, 5);
}

light.target.position.set(-5, 0, 0);
light.castShadow = true;
scene.add(light);
scene.add(light.target);



let controls = new OrbitControls(camera, renderer.domElement);


//let axes = new THREE.AxisHelper(50);
//scene.add( axes );




const loader = new GLTFLoader();
let referenceSize = 0

if (fileName === "gibson_firebird_v_electric_guitar") {
	referenceSize=8

}else{
	referenceSize = 5;
}
loader.load( `/static/models/${fileName}.glb`, function ( gltf ) {
	
	if (fileName === "gibson_firebird_v_electric_guitar") {
		gltf.scene.position.y = -2.5;
		gltf.scene.rotation.x = Math.PI / 9;
		gltf.scene.rotation.y = Math.PI / 11;

	}else if (fileName === "gibson_sg_guitar"){
		gltf.scene.rotation.z = (3 * Math.PI / 2);
		gltf.scene.position.y = 1;
	}else{
		gltf.scene.position.y = 1.5;
	}
	gltf.scene.traverse(function (child) {
        if (child.isMesh) {
            child.castShadow = true; 
        }
    });


	const boundingBox = new THREE.Box3().setFromObject(gltf.scene);
    const center = boundingBox.getCenter(new THREE.Vector3());

	const size = new THREE.Vector3();
    boundingBox.getSize(size);
	const scaleFactor = referenceSize / Math.max(size.x, size.y, size.z);
	gltf.scene.scale.set(scaleFactor, scaleFactor, scaleFactor);

    // Adjust camera position and look at the center of the model
    camera.position.set(center.x, center.y, center.z + 5); // Adjust the distance from the model
    camera.lookAt(center); // Make the camera look at the center of the model

	scene.add( gltf.scene );

}, 
	undefined, function ( error ) {
	console.error( error );
} );

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
  shadowSide: THREE.DoubleSide,
});
const mesh = new THREE.Mesh(planeGeo, planeMat);
mesh.rotation.x = Math.PI * -.5;
mesh.receiveShadow = true;
scene.add(mesh);
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
