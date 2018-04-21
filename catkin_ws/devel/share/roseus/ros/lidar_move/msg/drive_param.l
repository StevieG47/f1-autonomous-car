;; Auto-generated. Do not edit!


(when (boundp 'lidar_move::drive_param)
  (if (not (find-package "LIDAR_MOVE"))
    (make-package "LIDAR_MOVE"))
  (shadow 'drive_param (find-package "LIDAR_MOVE")))
(unless (find-package "LIDAR_MOVE::DRIVE_PARAM")
  (make-package "LIDAR_MOVE::DRIVE_PARAM"))

(in-package "ROS")
;;//! \htmlinclude drive_param.msg.html


(defclass lidar_move::drive_param
  :super ros::object
  :slots (_velocity _angle ))

(defmethod lidar_move::drive_param
  (:init
   (&key
    ((:velocity __velocity) 0.0)
    ((:angle __angle) 0.0)
    )
   (send-super :init)
   (setq _velocity (float __velocity))
   (setq _angle (float __angle))
   self)
  (:velocity
   (&optional __velocity)
   (if __velocity (setq _velocity __velocity)) _velocity)
  (:angle
   (&optional __angle)
   (if __angle (setq _angle __angle)) _angle)
  (:serialization-length
   ()
   (+
    ;; float32 _velocity
    4
    ;; float32 _angle
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _velocity
       (sys::poke _velocity (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _angle
       (sys::poke _angle (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _velocity
     (setq _velocity (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _angle
     (setq _angle (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get lidar_move::drive_param :md5sum-) "23ee9ebc4f65684302501539608c3833")
(setf (get lidar_move::drive_param :datatype-) "lidar_move/drive_param")
(setf (get lidar_move::drive_param :definition-)
      "float32 velocity
float32 angle

")



(provide :lidar_move/drive_param "23ee9ebc4f65684302501539608c3833")


