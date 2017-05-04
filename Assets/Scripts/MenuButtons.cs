using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class MenuButtons : MonoBehaviour {



    public void PlayGame() {
        SceneManager.LoadScene("Scene2");
    }

    public void GameEnd() {
        SceneManager.LoadScene("Scene3");
    }

    public void PlayAgain() {
        SceneManager.LoadScene("Scene1");
    }

    void endGameScreen() {

    }
}
