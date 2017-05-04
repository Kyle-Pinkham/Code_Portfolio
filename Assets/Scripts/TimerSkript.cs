using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class TimerSkript : MonoBehaviour {

    //public static TimerSkript control;
    public Text timer;
    float timeLeft = 185;

    //void Awake() {
    //    if (control == null) {
    //        DontDestroyOnLoad(gameObject);
    //        control = this;
    //    }
    //    else if (control != this) {
    //        Destroy(gameObject);
    //    }
    //}

    void Update() {
    timer.text = "Time Left: " + timeLeft.ToString("#.00");
        timeLeft -= (Time.deltaTime);
        if (timeLeft< 0)
            GameEnd();
    }

    void GameEnd() {
    SceneManager.LoadScene("Scene3");
    }
}
