//戦闘機のスプライト
var fighter;

//戦闘機の画像
var fighterImage;
// ブロックの画像
var blickImage;
// ブロックのアニメーション
var breakAnimation;

var blockgroup;


function preload() {
    //画像の読み込み
    fighterImage = loadImage('../img/rocket.png');
    // アニメーションの読み込み
    blockImage = loadImage('../img/isi.png');
   // breakAnimation = loadImage('../img/isi.png','../img/isi2.png');
    //breakAnimation.frameDelay = 1;
    //breakAmimationはループしない
    breakAnimation.looping = false;
}

function setup() {
    //横650縦600のキャンバスを作る
    createCanvas(650, 600);
    fighter = createSprite(300, 300);
    //画像をスプライトに張り付ける
    fighter.addImage(fighterImage);
    fighter.scale = 0.2;

    blockgroup = new Group();
    //キャンバスの上に８個のブロックをx座標が10~650の間、y座標が10~600の間にランダムで置く
    for (var i = 0; i < 8; i++) {
        var x = random(10, 650);
        var y = random(10, 600);
        var block = createSprite(x, y);
        // 画像をスプライトに付ける
        block.addImage(blockImage);
        // 画像の大きさを変える
        block.scale = 0.2;
        // グループにスプライトを追加
        blockgroup.add(block);

    }
}

function draw() {
    //キャンバスを塗りつぶす
    background(0);
    //スプライトを表示させる
    drawSprites();
    //戦闘機の操作
    fighterControl();
    // ブロックと衝突したら
    fighter.overlap(blockgroup, blockBreak);
}

// 戦闘機のコントロール
function fighterControl() {
    if (keyDown('RIGHT')) { //右矢印を押したとき
        //速度を10にする
        fighter.position.x += 10;
    } else if (keyDown('LEFT')) {//左矢印を押したとき
        //速度を-10にする
        fighter.position.x += -10;
    } else if (keyDown('UP')) {    //上矢印を押したとき
        fighter.position.y += -10;
    } else if (keyDown('DOWN')) {//下矢印を押したとき
        fighter.position.y += 10;
    }
    if (fighter.position.x > width - 30) { //右からはみ出ないように
        fighter.position.x = width - 30;
    } else if (fighter.position.x < 30) {  //左からはみ出ないように
        fighter.position.x = 30;
    }
}

// ブロックとの衝突処理
function blockBreak(fighter, block) {
    //壊れるブロックのスプライトをつくる
    var breakblock = createSprite(block.position.x, block.position.y);
    //アニメーションを読み込む
    //breakblock.addAnimation('break', breakAnimation);
    breakblock.scale = 0.2;
    //bkockスプライトを消す
    block.remove();
}