using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class RandomNumScript : MonoBehaviour {

    public float delay = 2.5f;
    public GameObject Circle;
    public GUIContent Canvas;

    private float randVal;

    void Start() {
        InvokeRepeating("Spawn", delay, delay);

    }

    void Spawn() {
        Instantiate(Circle, new Vector2(Random.Range(-7, 7), 10), Quaternion.identity);
    }
}
