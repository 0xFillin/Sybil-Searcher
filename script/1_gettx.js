const axios = require('axios');
const fs = require('fs');
const path = require('path');

const scanAPIKEY = ''; // API KEY {CHAIN}SCAN
const contractAddress = ''; // TOKEN CM
const startBlock = 72635645; // START BLOCK
const endBlock = 134246281; // LAST BLOCK
const blockSize = 80000;

async function getInteractedAddresses(start, end, blockSize) {
    let currentBlock = start;
    let blockCounter = 0;
    while (currentBlock <= end) {
        const url = `https://api.arbiscan.io/api?module=account&action=txlist&address=${contractAddress}&startblock=${currentBlock}&endblock=${Math.min(currentBlock + blockSize - 1, end)}&sort=asc&apikey=${scanAPIKEY}`;
        try {
            const response = await axios.get(url);
            const transactions = response.data.result || [];

            const addresses = new Set();

            transactions.forEach((tx) => {
                console.log('Transaction:', tx);
                if (tx.functionName === 'transfer(address to, uint256 amount)') { // Change to the desired function (l2 - transfer(address to, uint256 amount))
                    addresses.add(`${tx.from},${tx.input}`); // Change to the desired data
                }
            });

            const folderPath = path.join(__dirname, 'airdrop');
            if (!fs.existsSync(folderPath)) {
                fs.mkdirSync(folderPath); // Create a folder if it does not exist
            }

            const blockFileName = path.join(folderPath, `block_${currentBlock}_${currentBlock + blockSize - 1}.txt`);
            fs.writeFileSync(blockFileName, Array.from(addresses).join('\n'), 'utf-8');
        } catch (error) {
            console.error("Error occurred while fetching data:", error.message);
        }

        currentBlock += blockSize;
        blockCounter++;
        if (blockCounter % blockSize === 0) {
            console.log(`Saved addresses up to block ${currentBlock - 1}`);
        }
    }
}

getInteractedAddresses(startBlock, endBlock, blockSize);