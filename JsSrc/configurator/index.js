import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { ViewHelper } from 'three/addons/helpers/ViewHelper.js';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';


//~ Get the query parameters from the URL ~//
const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
const fileName = urlParams.get('file_name');

//~ Set up initial dimensions for the renderer ~//
let width = window.innerWidth;
let height =window.innerWidth ;

//~ Create a WebGLRenderer ~//
let renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setPixelRatio( window.devicePixelRatio );
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap;
renderer.autoClear = false;
renderer.setSize(width, height);
document.body.appendChild(renderer.domElement);

//~ Create a new scene and set its background color and fog ~//
let scene = new THREE.Scene();
//scene.background = new THREE.Color(0xfffafa );
//scene.fog = new THREE.Fog( 0xfffafa , 15, 50 );



//~ Create a new perspective camera and set position ~//
let camera = new THREE.PerspectiveCamera(75, width / height, 0.1, 10000);
camera.position.z = 30;
scene.add(camera);

//~ Create an AmbientLight to simulate global illumination ~//
let helper = new ViewHelper( camera, renderer.domElement );
const skycolor = 0xFFFFFF;
const skyintensity = 4;
const skylight = new THREE.AmbientLight(skycolor, skyintensity);
scene.add(skylight);

//~ Create a DirectionalLight ~//
const color = 0xFFFFFF;
const intensity = 6;
const light = new THREE.DirectionalLight(color, intensity);
light.position.set(0, 3, 5);

light.target.position.set(-5, 0, 0);
light.castShadow = true;
scene.add(light);
scene.add(light.target);


//~ Create OrbitControls to enable camera manipulation ~//
const controls = new OrbitControls( camera, renderer.domElement );
controls.maxDistance = 50;//~ Max zoom out distance ~//
controls.update();



//let axes = new THREE.AxisHelper(50);
//scene.add( axes );



//~ Load 3D model using GLTFLoader ~//
const loader = new GLTFLoader();
let referenceSize = 0

if (fileName === "gibson_firebird_v_electric_guitar") {
	referenceSize=35

}else{
	referenceSize = 50;
}
loader.load( `/static/models/${fileName}.glb`, function ( gltf ) {
	
	if (fileName === "gibson_firebird_v_electric_guitar") {
		gltf.scene.position.y = -1;
		//gltf.scene.rotation.x = Math.PI / 9;
		gltf.scene.rotation.y =Math.PI / 2;
		console.log(gltf.scene.rotation.z)
	}else if (fileName === "gibson_sg_guitar"){
		gltf.scene.rotation.z = 250;
		console.log(gltf.scene.rotation.z)
		gltf.scene.position.y = 1;
	}else{
		gltf.scene.position.y = 2;
		gltf.scene.rotation.x = Math.PI / 9;
	}
	//~ Traverse through model's children to enable shadow casting ~//
	gltf.scene.traverse(function (child) {
        if (child.isMesh) {
            child.castShadow = true; 
        }
    });

	//~ Calculate bounding box of the model and adjust its size and position ~//	
	const boundingBox = new THREE.Box3().setFromObject(gltf.scene);
    const center = boundingBox.getCenter(new THREE.Vector3());
	const size = new THREE.Vector3();
    boundingBox.getSize(size);
	const scaleFactor = referenceSize / Math.max(size.x, size.y, size.z);
	gltf.scene.scale.set(scaleFactor, scaleFactor, scaleFactor);

    //~ Adjust camera position and look at the center of the model ~//
    camera.position.set(center.x, center.y, center.z + 5); //~ Adjust distance from the model ~//
    camera.lookAt(center);

	//~ Add loaded model to the scene ~//
	scene.add( gltf.scene );

}, 
	//~Error loggin ~//
	undefined, function ( error ) {
	console.error( error );
} );


//~ Set up and add plane with texture to the scene (Ground) ~//
const planeSize = 80;
const texloader = new THREE.TextureLoader();
const texture = texloader.load('/static/models/resources/floor2.jpg');
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
//scene.add(mesh);
resize();
animate();


const backgroundloader = new THREE.TextureLoader();
const backgroundtexture = backgroundloader.load('/static/models/resources/castle_zavelstein_cellar.jpg',);
backgroundtexture.mapping = THREE.EquirectangularReflectionMapping;
backgroundtexture.colorSpace = THREE.SRGBColorSpace;
scene.background = backgroundtexture;

//~ Resize function to handle window resize events ~//
window.addEventListener('resize',resize);
function resize(){
	let w = window.innerWidth;
	let h = window.innerHeight * 0.925;
	renderer.setSize(w,h);
	camera.aspect = w / h;
	camera.updateProjectionMatrix();
}

//~ Animation loop function ~//
function animate() {
	//~ Check camera position and toggle visibility of the plane ~//
	const cameraPosition = new THREE.Vector3();
    cameraPosition.setFromMatrixPosition(camera.matrixWorld);

    if (cameraPosition.y < 0) {
        mesh.visible = false;
    } else {
        mesh.visible = true;
    }

	//~ Render scene and update controls ~//
    renderer.render(scene, camera);
	helper.render( renderer );
    controls.update();
    requestAnimationFrame(animate);//~ Request animation frame for smooth animation ~//
}
