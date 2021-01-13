import glob
import cv2
import predict


# アルコマーカーを識別させる関数
def aruco_marker(image):
    aruco = cv2.aruco
    # アルコマーカの辞書作成
    dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_100)
    # アルコマーカー識別
    corners, ids, rejectedImgPoints = aruco.detectMarkers(image, dictionary)
    aruco.drawDetectedMarkers(image, corners, ids)

    if ids is None:
        ids_length = 0
    else:
        ids_length = len(ids)
    # print(ids_length)

    return image, ids_length

# 画像を表示する関数
def image_show(image):
    cv2.imshow('frame', image)
    # 500msで表示を切り替え
    cv2.waitKey(500)
    cv2.destroyAllWindows()


# 画像を保存する関数
def image_write(image, image_dir, i):
    # ファイル名を "aruco_0x.png" の様に作る
    fileName = image_dir + "out_" + str(i).zfill(2) + ".jpg"
    cv2.imwrite(fileName, image)


weights_path = 'fpn_inception.h5'
predictor_one = predict.Predictor(weights_path=weights_path)


if __name__ == '__main__':

    input_dir_base = "D:\\workspace\\qwatch_video\\201216_experiment\\picture\\1280p\\speed6\\"
    output_dir_base = input_dir_base + "DeblurGAN\\"

    number = ["50", "100", "150", "200", "250"]

    for i in range(len(number)):
        input_dir = input_dir_base + number[i] + "\\"

        output_dir = output_dir_base + number[i] + "\\"
        output_dir_aruco = output_dir_base + "output_" + number[i] + "\\"

        result = []
        count = 0
        all = 0

        # 指定したフォルダ内の画像を順番にすべて読み込む
        files = glob.glob(input_dir + "*")
        for f in files:
            count = count + 1
            # 入力画像の読み込み
            image = cv2.imread(f)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            # cv2.imshow("input", image)
            # cv2.waitKey(500)

            # ブレ除去，表示，保存
            output_image = predict.pred_one_image(img=image)
            output_image = cv2.cvtColor(output_image, cv2.COLOR_RGB2BGR)
            image_show(output_image)
            image_write(output_image, output_dir, count)

            # OpenCV_aruco処理，表示，保存
            output_image_aruco, ids_length = aruco_marker(output_image)
            image_show(output_image_aruco)
            image_write(output_image_aruco, output_dir_aruco, count)

            result.append([ids_length * 5])
            all = all + ids_length * 5

        print(len(files))
        average = all/len(files)
        print(number[i], average)
        print(result)