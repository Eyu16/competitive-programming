
var MyStack = function() {
    this.stackSize = 0;
    this.stackCapacity = 5;
    this.stack = [];
    this.topp = -1;
};

/** 
 * @param {number} x
 * @return {void}
 */
MyStack.prototype.push = function(x) {
    if(this.stackSize === this.stackCapacity) return;
    else{
        this.topp++;
        this.stack[this.topp] = x;
        this.stackSize++;  
    }
};

/**
 * @return {number}
 */
MyStack.prototype.pop = function() {
    let x = this.stack[this.topp];
    this.topp--;
    this.stackSize--;
    return x;
    
};

/**
 * @return {number}
 */
MyStack.prototype.top = function() {
    x = this.stack[this.topp];
       return x;
    
};

/**
 * @return {boolean}
 */
MyStack.prototype.empty = function() {
    if(this.stackSize === 0) return true;
    else return false;
};

/** 
 * Your MyStack object will be instantiated and called as such:
 * var obj = new MyStack()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.empty()
 */