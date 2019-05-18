## Cookies vs. SessionStorage vs. LocalStorage

These three are all different types of frontend storage you can use to cache data.

* LocalStorage
    * Should be viewed as an extension of cookies but stronger. Has **5MB of data opposed to 4KB cookie.**
    * Changes persist until explicitly deleted.
    * Same origin policy
    ```javascript
    window.localStorage
    ```
* SessionStorage
    * Similar to LocalStorage, but only persists for the life of the tab.
    * Same origin policy
    ```javascript
    window.sessionStorage
    ```
* Cookies
    * Expiration can be set
    * Must be under 4KB
    * Sent back for every request