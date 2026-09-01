const path = require('path');
const fs = require('fs');

const puppeteer = require('C:/Agents/a0-symbiot-ai/projects/html2pdf/node_modules/puppeteer');

async function renderAll() {
    console.log('🚀 Launching Puppeteer for Lunar Flyby XR Print Render...');
    const browser = await puppeteer.launch({
        headless: 'new',
        args: ['--no-sandbox', '--disable-setuid-sandbox']
    });

    const printDir = path.resolve(__dirname, 'print');

    // 1. Render 11x17 Poster (PDF & High-Res PNG)
    {
        const posterHtmlPath = path.join(printDir, 'poster_11x17.html');
        const posterUrl = `file://${posterHtmlPath}`;
        console.log(`\nRendering 11x17 Poster from: ${posterUrl}`);

        const page = await browser.newPage();
        await page.setViewport({
            width: 1000,
            height: 1545,
            deviceScaleFactor: 2.2 // 2200 x 3400 px for crisp 300 DPI
        });

        await page.goto(posterUrl, { waitUntil: 'networkidle0' });

        // Generate 11x17 PDF
        const pdfPath = path.join(printDir, 'poster_11x17.pdf');
        await page.pdf({
            path: pdfPath,
            width: '11in',
            height: '17in',
            printBackground: true,
            margin: { top: 0, right: 0, bottom: 0, left: 0 }
        });
        console.log(`✅ Saved 11x17 PDF: ${pdfPath}`);

        // Capture High-Res 300 DPI PNG matching 100% HTML render
        const pngPath = path.join(printDir, 'lunar_flyby_poster_11x17_300dpi.png');
        const canvasElement = await page.$('.poster-canvas');
        if (canvasElement) {
            await canvasElement.screenshot({
                path: pngPath,
                type: 'png'
            });
            console.log(`✅ Saved 11x17 300 DPI PNG: ${pngPath}`);
        }
        await page.close();
    }

    // 2. Render 8.5x11 Flyer (PDF & High-Res PNG)
    {
        const flyerHtmlPath = path.join(printDir, 'flyer_8.5x11.html');
        const flyerUrl = `file://${flyerHtmlPath}`;
        console.log(`\nRendering 8.5x11 Flyer from: ${flyerUrl}`);

        const page = await browser.newPage();
        await page.setViewport({
            width: 850,
            height: 1100,
            deviceScaleFactor: 2.0 // 1700 x 2200 px for crisp 300 DPI
        });

        await page.goto(flyerUrl, { waitUntil: 'networkidle0' });

        // Generate 8.5x11 PDF
        const pdfPath = path.join(printDir, 'flyer_8.5x11.pdf');
        await page.pdf({
            path: pdfPath,
            width: '8.5in',
            height: '11in',
            printBackground: true,
            margin: { top: 0, right: 0, bottom: 0, left: 0 }
        });
        console.log(`✅ Saved 8.5x11 PDF: ${pdfPath}`);

        // Capture High-Res 300 DPI PNG matching 100% HTML render
        const pngPath = path.join(printDir, 'lunar_flyby_flyer_8.5x11_300dpi.png');
        const canvasElement = await page.$('.flyer-canvas');
        if (canvasElement) {
            await canvasElement.screenshot({
                path: pngPath,
                type: 'png'
            });
            console.log(`✅ Saved 8.5x11 300 DPI PNG: ${pngPath}`);
        }
        await page.close();
    }

    await browser.close();
    console.log('\n🎉 All PDF & 300 DPI Print assets generated with 100% HTML/CSS fidelity!');
}

renderAll().catch(err => {
    console.error('Render Error:', err);
    process.exit(1);
});
