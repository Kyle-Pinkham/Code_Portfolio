using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DestrcutionScript : MonoBehaviour {

    public GameObject Circle;


    void OnTriggerEnter2D() {
        Renderer[] renderers = GetComponentsInChildren<Renderer>();
        foreach (Renderer r in renderers)
            r.enabled = false;
        AudioSource audioFile = Circle.GetComponentInChildren<AudioSource>();
        audioFile.Play();
        Object.Destroy(gameObject, 0.5f);
        Debug.Log("death");
    }

    
}
