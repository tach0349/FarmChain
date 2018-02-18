pragma solidity ^0.4.17;

import "/Users/Ray/farmChain/node_modules/zeppelin-solidity/contracts/token/ERC721Token.sol";

contract Agricoin is ERC721Token{

	string productName;
	uint productWeight;
	uint value;

	function Agricoin(string _productName, uint _productWeight, uint _value){
		productName = _productName;
		productWeight = _productWeight;
		value = _value;
	}

}
