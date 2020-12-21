pragma solidity ^0.4.21;
//developed and compiled in remix.ethereum.org online
contract Greeter {
    string public greeting;

    function greeter() public
    {
        greeting = 'Hello contracts';
    }

    function setGreeting (string _greeting) public
    {
        greeting = _greeting;
    }

    function greet() view public returns (string) {
        return greeting;
    }

}