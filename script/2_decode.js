const fs = require('fs');
const Web3 = require('web3').default;
const web3 = new Web3(new Web3.providers.HttpProvider('https://arbitrum-mainnet.infura.io/v3/'));


// ABI CONCTRACT
const abi = [
    {
        "constant": false,
        "inputs": [
            {
                "name": "_to",
                "type": "address"
            },
            {
                "name": "_value",
                "type": "uint256"
            }
        ],
        "name": "transfer",
        "outputs": [],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    }
];


async function decodeTransactions() {
    try {
        const files = fs.readdirSync('./airdrop');

        const csvStream = fs.createWriteStream('decoded_transactions.csv');
        csvStream.write('address,to,value\n');

        for (const file of files) {
            const data = fs.readFileSync(`./airdrop/${file}`, 'utf-8').trim().split('\n');

            for (const line of data) {
                if (line.trim() === '') continue; 

                const [address, input] = line.split(',');

                try {
                    const decodedData = web3.eth.abi.decodeParameters(['address', 'uint256'], input.slice(10));
                    const to = decodedData[0];
                    const value = decodedData[1].toString(); 
                    csvStream.write(`${address},${to},${value}\n`);
                } catch (error) {
                    console.error(`Error decoding transaction for address ${address}: ${error.message}`);
                }
            }
        }

        csvStream.end();
        console.log('Decoding completed. Check decoded_transactions.csv file.');
    } catch (error) {
        console.error(`An error occurred: ${error.message}`);
    }
}

decodeTransactions().catch(console.error);