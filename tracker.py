import cv2
import sys

# 1. إنشاء متعقب الكائنات (Tracker)
# خوارزمية CSRT دقيقة جداً ومناسبة لتتبع الأجسام المتنوعة
tracker = cv2.TrackerCSRT_create()

# 2. تشغيل الكاميرا (أو يمكنك وضع مسار فيديو بدلاً من 0 مثل "video.mp4")
video = cv2.VideoCapture(0)

if not video.isOpened():
    print("خطأ: لا يمكن فتح الكاميرا!")
    sys.exit()

# قراءة الإطار الأول فقط لتحديد الجسم المراد تتبعه
ok, frame = video.read()
if not ok:
    print('خطأ: لا يمكن قراءة ملف الفيديو/الكاميرا')
    sys.exit()

# 3. فتح نافذة تطلب منك تحديد الجسم بالفأرة
# ارسمي مربعاً حول الجسم الذي تريدين تتبعه (مثلاً وجهكِ أو قطة أو ريموت..) ثم اضغطي ENTER أو SPACE
# لإلغاء التحديد واختيار منطقة أخرى، اضغطي على زر c
bbox = cv2.selectROI("Tracking Window", frame, fromCenter=False, showCrosshair=True)

# تهيئة المتعقب بالمربع الذي قمتِ بتحديده
ok = tracker.init(frame, bbox)
cv2.destroyWindow("Tracking Window") # إغلاق نافذة التحديد والبدء بالتتبع الفعلي

while True:
    # قراءة إطار تلو الآخر من الفيديو
    ok, frame = video.read()
    if not ok:
        break
        
    # قياس الوقت المستغرق لمعرفة سرعة المعالجة (FPS)
    timer = cv2.getTickCount()

    # تحديث موقع المتعقب بناءً على الإطار الجديد
    ok, bbox = tracker.update(frame)

    # حساب معدل الإطارات في الثانية (FPS)
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)

    # إذا نجح المتعقب في إيجاد الجسم في الإطار الجديد
    if ok:
        # الإحداثيات الجديدة للجسم المتتبع
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        # رسم مربع أخضر حول الجسم المتتبع
        cv2.rectangle(frame, p1, p2, (0, 255, 0), 2, 1)
        # كتابة اسم الحالة
        cv2.putText(frame, "Tracking...", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)
    else:
        # في حال فقدان الجسم (مثلاً خرج من كادر الكاميرا)
        cv2.putText(frame, "Tracking failure detected", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

    # عرض نوع الخوارزمية ومعدل الـ FPS على الشاشة
    cv2.putText(frame, "CSRT Tracker", (100, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2)
    cv2.putText(frame, "FPS : " + str(int(fps)), (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2)

    # عرض الفيديو التفاعلي المباشر
    cv2.imshow("Object Tracking", frame)

    # للخروج من البرنامج، اضغطي على مفتاح 'ESC' من لوحة المفاتيح
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break

video.release()
cv2.destroyAllWindows()