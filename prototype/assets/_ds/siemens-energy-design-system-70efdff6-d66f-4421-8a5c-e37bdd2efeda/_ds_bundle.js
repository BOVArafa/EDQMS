/* @ds-bundle: {"format":4,"namespace":"SiemensEnergyDesignSystem_70efdf","components":[{"name":"Button","sourcePath":"components/buttons/Button.jsx"},{"name":"IconButton","sourcePath":"components/buttons/IconButton.jsx"},{"name":"Avatar","sourcePath":"components/core/Avatar.jsx"},{"name":"Card","sourcePath":"components/core/Card.jsx"},{"name":"Icon","sourcePath":"components/core/Icon.jsx"},{"name":"Badge","sourcePath":"components/feedback/Badge.jsx"},{"name":"EmptyState","sourcePath":"components/feedback/EmptyState.jsx"},{"name":"StatusDot","sourcePath":"components/feedback/StatusDot.jsx"},{"name":"Checkbox","sourcePath":"components/forms/Checkbox.jsx"},{"name":"Select","sourcePath":"components/forms/Select.jsx"},{"name":"Switch","sourcePath":"components/forms/Switch.jsx"},{"name":"TextInput","sourcePath":"components/forms/TextInput.jsx"},{"name":"Tabs","sourcePath":"components/navigation/Tabs.jsx"}],"sourceHashes":{"assets/icon-data.js":"9c1e75d50fe2","components/buttons/Button.jsx":"3daf85568525","components/buttons/IconButton.jsx":"0e04fd7c5e54","components/core/Avatar.jsx":"82374946c348","components/core/Card.jsx":"f57213eb2c65","components/core/Icon.jsx":"910e8d7ae079","components/feedback/Badge.jsx":"6e6ab633b1a7","components/feedback/EmptyState.jsx":"ff5dd77c1b6a","components/feedback/StatusDot.jsx":"1ad2b3227663","components/forms/Checkbox.jsx":"942b9298b5e4","components/forms/Select.jsx":"fa957a071b5d","components/forms/Switch.jsx":"1fd031fa2cc2","components/forms/TextInput.jsx":"578784f2bef7","components/navigation/Tabs.jsx":"8f29fbe0a0b6","ui_kits/asset-monitoring/AppHeader.jsx":"42c24c9142a9","ui_kits/asset-monitoring/AssetTable.jsx":"c086be4f09f9","ui_kits/asset-monitoring/Screens.jsx":"2fc254d2c2a4"},"inlinedExternals":[],"unexposedExports":[]} */

(() => {

const __ds_ns = (window.SiemensEnergyDesignSystem_70efdf = window.SiemensEnergyDesignSystem_70efdf || {});

const __ds_scope = {};

(__ds_ns.__errors = __ds_ns.__errors || []);

// assets/icon-data.js
try { (() => {
window.__SE_ICONS__ = {
  "account": {
    "viewBox": "0 0 512 512",
    "inner": "<path d=\"M256,32c-59.83,0-116.08,23.3-158.39,65.61-42.31,42.31-65.61,98.56-65.61,158.39s23.3,116.08,65.61,158.39c42.31,42.31,98.56,65.61,158.39,65.61s116.08-23.3,158.39-65.61,65.61-98.56,65.61-158.39-23.3-116.08-65.61-158.39c-42.31-42.31-98.56-65.61-158.39-65.61ZM129.5,400.3c25.35-13.84,75.54-37.01,127.5-37.01,60.39,0,105.19,22.37,126.76,35.9-33.96,30.34-78.74,48.81-127.76,48.81s-92.69-18.02-126.5-47.7ZM406.16,375.5c-22.98-15.47-75.58-44.21-149.16-44.21-65.16,0-125.43,30.58-150.42,45.13-26.61-32.96-42.58-74.86-42.58-120.42,0-105.87,86.13-192,192-192s192,86.13,192,192c0,45.14-15.67,86.69-41.84,119.5Z\"></path><path d=\"M256,133.71c-45.77,0-83,37.23-83,83s37.23,83,83,83,83-37.23,83-83-37.23-83-83-83ZM256,267.71c-28.12,0-51-22.88-51-51s22.88-51,51-51,51,22.88,51,51-22.88,51-51,51Z\"></path>"
  },
  "account-filled": {
    "viewBox": "0 0 512 512",
    "inner": "<path d=\"M256,32c-59.83,0-116.08,23.3-158.39,65.61-42.31,42.31-65.61,98.56-65.61,158.39s23.3,116.08,65.61,158.39c42.31,42.31,98.56,65.61,158.39,65.61s116.08-23.3,158.39-65.61,65.61-98.56,65.61-158.39-23.3-116.08-65.61-158.39c-42.31-42.31-98.56-65.61-158.39-65.61ZM406.16,375.5c-22.98-15.47-75.58-44.21-149.16-44.21-65.16,0-125.43,30.58-150.42,45.13-26.61-32.96-42.58-74.86-42.58-120.42,0-105.87,86.13-192,192-192s192,86.13,192,192c0,45.14-15.67,86.69-41.84,119.5Z\"></path><path d=\"M256,133.71c-45.77,0-83,37.23-83,83s37.23,83,83,83,83-37.23,83-83-37.23-83-83-83Z\"></path>"
  },
  "alarm-filled": {
    "viewBox": "0 0 512 512",
    "inner": "<path d=\"M255.91,448.02c-9.03,0-17.93-2.38-25.95-7.03-7.8-4.53-14.32-11.04-18.84-18.84-4.43-7.64-1.83-17.43,5.81-21.87,7.64-4.43,17.43-1.83,21.87,5.81,1.73,2.99,4.23,5.49,7.22,7.22,4.59,2.67,9.95,3.38,15.08,2.02,5.13-1.36,9.43-4.65,12.09-9.24,4.43-7.64,14.22-10.25,21.87-5.81,7.64,4.43,10.25,14.22,5.81,21.87-6.95,11.99-18.16,20.55-31.55,24.11-4.44,1.18-8.94,1.76-13.41,1.76Z\"></path><path d=\"M432,368H80c-6.44,0-12.24-3.86-14.74-9.79s-1.2-12.78,3.29-17.39c.04-.05,10.2-10.79,23.31-34.7,12.12-22.1,29.31-60.25,42.39-116.57.72-3.54,6.85-32,23.15-60.77,23.67-41.76,57.26-64.13,97.18-64.75.47-.03.94-.04,1.41-.04.47,0,.95,0,1.41.04,39.92.62,73.51,22.99,97.18,64.75,16.31,28.78,22.44,57.25,23.16,60.77,7.24,31.15,20.45,76.57,42.39,116.56,13.11,23.91,23.27,34.65,23.37,34.76,4.49,4.61,5.76,11.43,3.26,17.36-2.5,5.93-8.34,9.76-14.77,9.76Z\"></path>"
  },
  "calendar": {
    "viewBox": "0 0 512 512",
    "inner": "<path d=\"M392.89,80h-40.89v-16c0-8.84-7.16-16-16-16s-16,7.16-16,16v16h-128v-16c0-8.84-7.16-16-16-16s-16,7.16-16,16v16h-40.89c-30.39,0-55.11,24.72-55.11,55.11v273.78c0,30.39,24.72,55.11,55.11,55.11h273.78c30.39,0,55.11-24.72,55.11-55.11V135.11c0-30.39-24.72-55.11-55.11-55.11ZM119.11,112h40.89v16c0,8.84,7.16,16,16,16s16-7.16,16-16v-16h128v16c0,8.84,7.16,16,16,16s16-7.16,16-16v-16h40.89c12.74,0,23.11,10.37,23.11,23.11v56.78H96v-56.78c0-12.74,10.37-23.11,23.11-23.11ZM392.89,432H119.11c-12.74,0-23.11-10.37-23.11-23.11v-185h320v185c0,12.74-10.37,23.11-23.11,23.11Z\"></path><path d=\"M352.79,265.66c-13.56,0-24.54,11.01-24.44,24.58,0,13.37,10.94,24.31,24.44,24.31s24.45-10.95,24.45-24.44-10.94-24.45-24.45-24.45Z\"></path><path d=\"M256.26,265.66c-13.56,0-24.54,11.01-24.44,24.58,0,13.37,10.95,24.31,24.44,24.31s24.45-10.95,24.45-24.44-10.95-24.44-24.45-24.44Z\"></path><path d=\"M256.26,342.88c-13.56,0-24.54,11.01-24.44,24.58,0,13.37,10.95,24.31,24.44,24.31s24.45-10.95,24.45-24.44-10.95-24.45-24.45-24.45Z\"></path><path d=\"M159.74,342.88c-13.56,0-24.54,11.01-24.44,24.58,0,13.37,10.95,24.31,24.44,24.31s24.44-10.95,24.44-24.44-10.95-24.45-24.44-24.45Z\"></path>"
  },
  "cancel": {
    "viewBox": "0 0 512 512",
    "inner": "<path d=\"M411.31,100.69c-6.25-6.25-16.38-6.25-22.63,0l-132.69,132.69L123.31,100.69c-6.25-6.25-16.38-6.25-22.63,0-6.25,6.25-6.25,16.38,0,22.63l132.69,132.69-132.69,132.69c-6.25,6.25-6.25,16.38,0,22.63,3.12,3.12,7.22,4.69,11.31,4.69s8.19-1.56,11.31-4.69l132.69-132.69,132.69,132.69c3.12,3.12,7.22,4.69,11.31,4.69s8.19-1.56,11.31-4.69c6.25-6.25,6.25-16.38,0-22.63l-132.69-132.69,132.69-132.69c6.25-6.25,6.25-16.38,0-22.63Z\"></path>"
  },
  "dashboard": {
    "viewBox": "0 0 512 512",
    "inner": "<path d=\"M256,480.02c-29.58,0-59.14-5.94-87.21-17.81-55.1-23.3-97.83-66.66-120.32-122.1s-22.04-116.31,1.26-171.41c22.44-53.07,63.89-95,116.71-118.05,8.1-3.54,17.53.17,21.06,8.27,3.53,8.1-.17,17.53-8.27,21.06-45.27,19.76-80.79,55.69-100.03,101.18-19.97,47.23-20.35,99.41-1.08,146.92s55.9,84.68,103.13,104.65c47.23,19.97,99.41,20.35,146.92,1.08,47.52-19.27,84.68-55.9,104.65-103.13,3.44-8.14,12.83-11.94,20.97-8.5,8.14,3.44,11.95,12.83,8.51,20.97-23.3,55.1-66.66,97.83-122.1,120.32-27.2,11.03-55.71,16.55-84.21,16.55Z\"></path><path d=\"M464,272.02h-207.97c-8.84,0-16-7.16-16-16V48.05c0-8.84,7.16-16,16-16,59.82,0,116.07,23.3,158.37,65.6,42.3,42.3,65.6,98.54,65.6,158.37,0,8.84-7.16,16-16,16ZM272.03,240.02h175.31c-7.72-93.12-82.19-167.59-175.31-175.31v175.31Z\"></path>"
  },
  "delete": {
    "viewBox": "0 0 512 512",
    "inner": "<path d=\"M159.64,448h192.72c26.47,0,48-21.53,48-48v-240h31.64c8.84,0,16-7.16,16-16s-7.16-16-16-16h-92.31v-16c0-26.47-21.53-48-48-48h-71.38c-26.47,0-48,21.53-48,48v16h-92.31c-8.84,0-16,7.16-16,16s7.16,16,16,16h31.64v240c0,26.47,21.53,48,48,48ZM368.36,400c0,8.82-7.18,16-16,16h-192.72c-8.82,0-16-7.18-16-16v-240h224.72v240ZM204.31,112c0-8.82,7.18-16,16-16h71.38c8.82,0,16,7.18,16,16v16h-103.38v-16Z\"></path><path d=\"M208,368c8.84,0,16-7.16,16-16v-128c0-8.84-7.16-16-16-16s-16,7.16-16,16v128c0,8.84,7.16,16,16,16Z\"></path><path d=\"M304,368c8.84,0,16-7.16,16-16v-128c0-8.84-7.16-16-16-16s-16,7.16-16,16v128c0,8.84,7.16,16,16,16Z\"></path>"
  },
  "document": {
    "viewBox": "0 0 512 512",
    "inner": "<path d=\"M275.33,64h-147.14c-17.75,0-32.19,14.35-32.19,32v320c0,17.65,14.44,32,32.19,32h255.62c17.75,0,32.19-14.35,32.19-32v-212.8c0-4.28-1.71-8.38-4.75-11.38l-124.67-123.2c-3-2.96-7.04-4.62-11.25-4.62ZM288,115.02l77.9,76.98h-77.9v-76.98ZM383.81,416h-255.62c-.07,0-.13-.01-.16-.01-.02,0-.03,0-.03.01l-.03-319.92c.04-.06.11-.08.22-.08h127.81v112c0,8.84,7.16,16,16,16h112l.02,191.92c-.04.06-.11.08-.22.08Z\"></path>"
  },
  "down-1": {
    "viewBox": "0 0 512 512",
    "inner": "<path d=\"M242.54,376.65c2.94,4.58,8.01,7.35,13.46,7.35s10.51-2.77,13.46-7.35l144-224c3.17-4.92,3.39-11.18.58-16.32s-8.19-8.33-14.04-8.33H112c-5.85,0-11.24,3.2-14.04,8.33s-2.58,11.4.58,16.32l144,224ZM370.69,160l-114.69,178.41-114.69-178.41h229.39Z\"></path>"
  },
  "download": {
    "viewBox": "0 0 512 512",
    "inner": "<path d=\"M256,64c-8.84,0-16,7.16-16,16v201.26l-70.46-70.46c-6.25-6.25-16.38-6.25-22.63,0-6.25,6.25-6.25,16.38,0,22.63l97.78,97.78c3.12,3.12,7.22,4.69,11.31,4.69s8.19-1.56,11.31-4.69l97.78-97.78c6.25-6.25,6.25-16.38,0-22.63-6.25-6.25-16.38-6.25-22.63,0l-70.46,70.46V80c0-8.84-7.16-16-16-16Z\"></path><path d=\"M112,448h288c26.47,0,48-21.53,48-48v-80c0-8.84-7.16-16-16-16s-16,7.16-16,16v80c0,8.82-7.18,16-16,16H112c-8.82,0-16-7.18-16-16v-80c0-8.84-7.16-16-16-16s-16,7.16-16,16v80c0,26.47,21.53,48,48,48Z\"></path>"
  },
  "edit": {
    "viewBox": "0 0 512 512",
    "inner": "<path d=\"M428.61,83.39c-25.81-25.82-67.82-25.81-93.64,0l-239.66,239.66c-1.97,1.97-3.39,4.42-4.12,7.1l-26.63,97.64c-1.51,5.54.06,11.46,4.12,15.52,3.04,3.04,7.13,4.69,11.31,4.69,1.4,0,2.82-.19,4.21-.56l97.64-26.63c2.69-.73,5.13-2.15,7.1-4.12l239.66-239.66c25.82-25.82,25.82-67.82,0-93.64ZM117.27,356.15c16.68,8.24,30.34,21.94,38.57,38.58l-53.04,14.47,14.47-53.04ZM405.98,154.4l-223.05,223.05c-10.92-20.46-27.87-37.45-48.38-48.39l223.05-223.05c13.34-13.34,35.04-13.34,48.38,0,13.34,13.34,13.34,35.04,0,48.38Z\"></path>"
  },
  "filter": {
    "viewBox": "0 0 512 512",
    "inner": "<path d=\"M432,80H80c-8.84,0-16,7.16-16,16v64c0,4.94,2.28,9.6,6.18,12.63l137.82,107.2v116.17c0,5.65,2.98,10.88,7.83,13.76l64,38c2.52,1.49,5.34,2.24,8.17,2.24s5.46-.7,7.92-2.1c5-2.84,8.08-8.15,8.08-13.9v-154.17l137.82-107.2c3.9-3.03,6.18-7.69,6.18-12.63v-64c0-8.84-7.16-16-16-16ZM416,112v32H96v-32h320ZM278.18,259.37c-3.9,3.03-6.18,7.69-6.18,12.63v133.89l-32-19v-114.89c0-4.94-2.28-9.6-6.18-12.63l-107.19-83.37h258.73l-107.19,83.37Z\"></path>"
  },
  "home": {
    "viewBox": "0 0 512 512",
    "inner": "<path d=\"M425.25,167.91l-150.54-123.19c-10.81-8.83-26.53-8.84-37.4.01l-150.57,123.18c-14.46,11.83-22.74,29.33-22.74,48.01v184.08c0,26.46,21.53,48,48,48h96v-160h96v160h96c26.46,0,48-21.54,48-48v-184.08c0-18.68-8.29-36.18-22.75-48.01ZM416,400c0,8.82-7.18,16-16,16h-64v-144c0-8.84-7.17-16-16-16h-128c-8.84,0-16,7.16-16,16v144h-64c-8.83,0-16-7.18-16-16v-184.08c0-9.05,4.01-17.52,11.01-23.25l149-121.9,148.97,121.9c7,5.73,11.02,14.2,11.02,23.25v184.08Z\"></path>"
  },
  "menu": {
    "viewBox": "0 0 512 512",
    "inner": "<path d=\"M432,272H80c-8.84,0-16-7.16-16-16s7.16-16,16-16h352c8.84,0,16,7.16,16,16s-7.16,16-16,16Z\"></path><path d=\"M432,160H80c-8.84,0-16-7.16-16-16s7.16-16,16-16h352c8.84,0,16,7.16,16,16s-7.16,16-16,16Z\"></path><path d=\"M432,384H80c-8.84,0-16-7.16-16-16s7.16-16,16-16h352c8.84,0,16,7.16,16,16s-7.16,16-16,16Z\"></path>"
  },
  "plus": {
    "viewBox": "0 0 512 512",
    "inner": "<path d=\"M112,272h128v128c0,8.84,7.16,16,16,16s16-7.16,16-16v-128h128c8.84,0,16-7.16,16-16s-7.16-16-16-16h-128V112c0-8.84-7.16-16-16-16s-16,7.16-16,16v128H112c-8.84,0-16,7.16-16,16s7.16,16,16,16Z\"></path>"
  },
  "refresh": {
    "viewBox": "0 0 512 512",
    "inner": "<path d=\"M255.99,431.75c46.93,0,91.06-18.28,124.25-51.47,29.88-29.88,48-69.52,51.01-111.62,2.99-41.66-8.92-83.05-33.54-116.54-5.23-7.12-15.25-8.65-22.37-3.42-7.12,5.23-8.65,15.25-3.42,22.37,20.12,27.37,29.85,61.22,27.4,95.3-2.47,34.42-17.29,66.84-41.72,91.28-27.14,27.14-63.23,42.09-101.62,42.09s-74.48-14.95-101.62-42.09c-27.14-27.14-42.09-63.23-42.09-101.62s14.95-74.48,42.09-101.62,62.57-41.81,100.56-42.09c7.17-.05,18.02-.07,28.51-.09,2.41,0,4.81,0,7.16-.01l-28.46,28.46c-6.25,6.25-6.25,16.38,0,22.63,3.12,3.12,7.22,4.69,11.31,4.69s8.19-1.56,11.31-4.69l52.12-52.12c6.25-6.25,6.25-16.38,0-22.63l-52.12-52.12c-6.25-6.25-16.38-6.25-22.63,0-6.25,6.25-6.25,16.38,0,22.63l21.17,21.17c-10.51.02-21.37.04-28.61.09-46.44.34-90.1,18.62-122.95,51.46-33.19,33.19-51.47,77.31-51.47,124.25s18.28,91.06,51.47,124.25c33.19,33.19,77.31,51.47,124.25,51.47Z\"></path>"
  },
  "right-1": {
    "viewBox": "0 0 512 512",
    "inner": "<path d=\"M136.33,414.04c2.4,1.31,5.03,1.96,7.67,1.96,3.02,0,6.02-.85,8.65-2.54l224-144c4.58-2.94,7.35-8.01,7.35-13.46s-2.77-10.51-7.35-13.46L152.65,98.54c-4.92-3.16-11.18-3.39-16.32-.58-5.14,2.8-8.33,8.19-8.33,14.04v288c0,5.85,3.2,11.24,8.33,14.04ZM160,141.31l178.41,114.69-178.41,114.69v-229.39Z\"></path>"
  },
  "search": {
    "viewBox": "0 0 512 512",
    "inner": "<path d=\"M240,416c42.77,0,82.03-15.34,112.56-40.81l68.12,68.12c3.12,3.12,7.22,4.69,11.31,4.69s8.19-1.56,11.31-4.69c6.25-6.25,6.25-16.38,0-22.63l-68.12-68.12c25.47-30.53,40.81-69.79,40.81-112.56,0-97.05-78.95-176-176-176S64,142.95,64,240s78.95,176,176,176ZM240,96c79.4,0,144,64.6,144,144s-64.6,144-144,144-144-64.6-144-144S160.6,96,240,96Z\"></path>"
  },
  "settings": {
    "viewBox": "0 0 512 512",
    "inner": "<defs></defs><path class=\"cls-1\" d=\"M224.48,474.55c-18.41,0-34.24-13.71-36.83-31.9l-4.88-34.08-.07-.19c-.39-1.08-1.75-1.86-2.15-2.07-5.7-2.89-11.42-6.23-17-9.93-.26-.18-1.23-.77-2.25-.77-.3,0-.57.05-.83.15l-31.84,12.8c-4.39,1.76-9.02,2.66-13.76,2.66-13.34,0-25.72-7.11-32.31-18.56l-31.59-54.7c-9.23-15.94-5.24-36.53,9.28-47.89l28.08-21.99-.08-1.07c-.29-3.91-.44-7.51-.44-11.01s.14-7.09.44-11.02l.08-1.07-28.08-21.99c-14.53-11.33-18.52-31.93-9.28-47.92l31.59-54.66c6.6-11.44,19.01-18.55,32.38-18.55,4.72,0,9.33.89,13.69,2.63l32.18,12.95h.39c.77,0,1.65-.29,2.37-.77,5.54-3.68,11.27-7.03,17.05-9.96.41-.22,1.73-.97,2.1-2.07l.06-.18,4.88-34.04c2.58-18.2,18.42-31.92,36.83-31.92h63.05c18.4,0,34.22,13.72,36.81,31.92l4.87,33.93.02.09c.3,1.26,1.85,2.08,2.15,2.23,5.77,2.89,11.49,6.21,16.97,9.88l.09.06c1.09.65,1.88.78,2.35.78h.39l32.2-12.9c4.37-1.75,8.98-2.64,13.7-2.64,13.34,0,25.74,7.11,32.34,18.56l31.62,54.66c9.24,15.96,5.25,36.57-9.28,47.92l-28.08,21.96.08,1.06c.3,4.06.44,7.67.44,11.04l-.07,4.17c-.07,2.13-.19,4.39-.37,6.87l-.08,1.06,28.08,21.96c14.52,11.37,18.51,31.97,9.28,47.92l-31.62,54.68c-6.6,11.46-18.98,18.57-32.32,18.57-4.73,0-9.35-.89-13.72-2.65l-32.14-12.92h-.39c-1.13,0-2.08.57-2.44.82-5.37,3.59-11.09,6.92-16.98,9.89-.41.19-1.88.98-2.2,2.21l-.03.11-4.87,33.97c-2.59,18.19-18.41,31.9-36.81,31.9h-63.05ZM161.29,361.43c7.48,0,14.8,2.22,21.17,6.42,4.63,3.08,9.08,5.68,13.61,7.95,11.19,5.72,18.88,16.23,20.57,28.11l4.88,33.88c.2,1.43,1.51,2.56,2.97,2.56h63.05c1.52,0,2.74-1.06,2.97-2.57l4.85-33.82c1.69-11.96,9.43-22.48,20.73-28.15,4.59-2.33,9.1-4.95,13.43-7.81,6.39-4.26,13.76-6.51,21.3-6.51,4.7,0,9.26.88,13.55,2.6l31.77,12.73c.34.14.7.21,1.08.21,1.06,0,2.09-.59,2.63-1.5l31.59-54.67c.74-1.28.42-2.95-.76-3.88l-35.51-27.77c-4.75-3.69-7.21-9.67-6.44-15.61.59-4.82,1.27-11.16,1.28-17.54l-.19-6.01c-.18-3.45-.53-7.14-1.09-11.67-.78-5.92,1.69-11.89,6.44-15.6l35.52-27.78c1.18-.91,1.51-2.55.76-3.81l-31.6-54.72c-.53-.92-1.55-1.51-2.59-1.51-.37,0-.73.07-1.06.22l-31.82,12.75c-4.28,1.74-8.83,2.62-13.52,2.62-7.51,0-14.88-2.26-21.31-6.54-4.58-3.01-8.99-5.57-13.5-7.83-11.26-5.66-18.99-16.17-20.68-28.13l-4.85-33.85c-.22-1.49-1.47-2.56-2.97-2.56h-63.05c-1.46,0-2.76,1.12-2.97,2.56l-4.88,33.88c-1.68,11.87-9.36,22.37-20.53,28.07-4.64,2.36-9.09,4.97-13.62,7.98-6.37,4.22-13.71,6.45-21.2,6.45-4.7,0-9.27-.88-13.58-2.61l-31.82-12.78c-.36-.14-.74-.21-1.11-.21-1.07,0-2.04.56-2.59,1.5l-31.59,54.67c-.74,1.29-.42,2.94.75,3.85l35.53,27.78c4.7,3.68,7.16,9.64,6.44,15.55-.6,4.86-1.28,11.26-1.28,17.67s.68,12.8,1.28,17.67c.72,5.91-1.74,11.86-6.44,15.54l-35.52,27.8c-1.16.9-1.48,2.56-.74,3.86l31.59,54.67c.53.91,1.52,1.47,2.59,1.47.39,0,.77-.07,1.14-.21l31.77-12.77c4.33-1.73,8.91-2.61,13.62-2.61ZM256,333.55c-42.76,0-77.55-34.79-77.55-77.55s34.79-77.55,77.55-77.55,77.55,34.79,77.55,77.55-34.79,77.55-77.55,77.55ZM256,212.68c-23.89,0-43.32,19.44-43.32,43.32s19.43,43.32,43.32,43.32,43.32-19.43,43.32-43.32-19.43-43.32-43.32-43.32Z\"></path>"
  },
  "upload": {
    "viewBox": "0 0 512 512",
    "inner": "<path d=\"M112,448h288c26.47,0,48-21.53,48-48v-80c0-8.84-7.16-16-16-16s-16,7.16-16,16v80c0,8.82-7.18,16-16,16H112c-8.82,0-16-7.18-16-16v-80c0-8.84-7.16-16-16-16s-16,7.16-16,16v80c0,26.47,21.53,48,48,48Z\"></path><path d=\"M256,336c8.84,0,16-7.16,16-16V118.63l70.46,70.46c3.12,3.12,7.22,4.69,11.31,4.69s8.19-1.56,11.31-4.69c6.25-6.25,6.25-16.38,0-22.63l-97.78-97.78c-6.25-6.25-16.38-6.25-22.63,0l-97.78,97.78c-6.25,6.25-6.25,16.38,0,22.63,6.25,6.25,16.38,6.25,22.63,0l70.46-70.46v201.37c0,8.84,7.16,16,16,16Z\"></path>"
  },
  "validation-critical-filled": {
    "viewBox": "0 0 512 512",
    "inner": "<path d=\"M466.28,150.21l-104.49-104.49c-8.52-8.52-19.85-13.21-31.9-13.21h-147.77c-12.05,0-23.38,4.69-31.91,13.22l-104.49,104.49c-8.52,8.52-13.21,19.85-13.21,31.9v147.77c0,12.05,4.69,23.38,13.22,31.9l104.49,104.49c8.52,8.52,19.85,13.21,31.9,13.21h147.77c12.05,0,23.38-4.69,31.91-13.22l104.49-104.49c8.52-8.52,13.22-19.85,13.22-31.9v-147.77c0-12.05-4.69-23.38-13.22-31.91ZM236,169.32c0-11.05,8.95-20,20-20s20,8.95,20,20v89.8c0,11.05-8.95,20-20,20s-20-8.95-20-20v-89.8ZM256.17,359.03h-.34c-13.16,0-23.83-10.75-23.83-24s10.67-24,23.83-24h.34c13.16,0,23.83,10.75,23.83,24s-10.67,24-23.83,24Z\"></path>"
  },
  "validation-information-filled": {
    "viewBox": "0 0 512 512",
    "inner": "<path d=\"M401,64H111c-25.92,0-47,21.08-47,47v290c0,25.92,21.08,47,47,47h290c25.92,0,47-21.08,47-47V111c0-25.92-21.08-47-47-47ZM276,336c0,11.05-8.95,20-20,20s-20-8.95-20-20v-80c0-11.05,8.95-20,20-20s20,8.95,20,20v80ZM256.17,204.32h-.34c-13.16,0-23.83-10.75-23.83-24s10.67-24,23.83-24h.34c13.16,0,23.83,10.75,23.83,24s-10.67,24-23.83,24Z\"></path>"
  },
  "validation-success-filled": {
    "viewBox": "0 0 512 512",
    "inner": "<path d=\"M414.39,97.61c-42.31-42.31-98.56-65.61-158.39-65.61s-116.08,23.3-158.39,65.61c-42.31,42.31-65.61,98.56-65.61,158.39s23.3,116.08,65.61,158.39c42.31,42.31,98.56,65.61,158.39,65.61s116.08-23.3,158.39-65.61c42.31-42.31,65.61-98.56,65.61-158.39s-23.3-116.08-65.61-158.39ZM360.14,216.27l-123.75,123.75c-3.91,3.91-9.02,5.86-14.14,5.86s-10.24-1.95-14.14-5.86l-56.25-56.25c-7.81-7.81-7.81-20.47,0-28.28,7.81-7.81,20.47-7.81,28.28,0l42.11,42.11,109.61-109.61c7.81-7.81,20.47-7.81,28.28,0s7.81,20.47,0,28.28Z\"></path>"
  },
  "validation-warning-filled": {
    "viewBox": "0 0 512 512",
    "inner": "<path d=\"M472.3,350.31c-.05-.08-.1-.17-.15-.25L305.11,71.19c-7.96-13.12-20.54-22.35-35.44-26-14.9-3.65-30.33-1.28-43.45,6.68-7.87,4.77-14.55,11.45-19.32,19.32-.02.03-.03.06-.05.09L39.85,350.06c-.05.08-.1.17-.15.25-15.84,27.42-6.41,62.62,21.02,78.46,8.53,4.93,18.24,7.59,28.09,7.69.07,0,.13,0,.2,0h334c.07,0,.13,0,.2,0,31.67-.35,57.15-26.39,56.8-58.06-.11-9.84-2.77-19.56-7.69-28.08ZM236,179.97c0-11.05,8.95-20,20-20s20,8.95,20,20v79.14c0,11.05-8.95,20-20,20s-20-8.95-20-20v-79.14ZM256.17,359.03h-.34c-13.16,0-23.83-10.75-23.83-24s10.67-24,23.83-24h.34c13.16,0,23.83,10.75,23.83,24s-10.67,24-23.83,24Z\"></path>"
  }
};
})(); } catch (e) { __ds_ns.__errors.push({ path: "assets/icon-data.js", error: String((e && e.message) || e) }); }

// components/buttons/Button.jsx
try { (() => {
const VARIANTS = {
  primary: {
    background: 'var(--se-action-primary)',
    color: 'var(--se-action-primary-text)',
    border: '1.5px solid transparent',
    hoverBg: 'var(--se-action-primary-hover)'
  },
  secondary: {
    background: 'var(--se-action-secondary)',
    color: 'var(--se-action-secondary-text)',
    border: '1.5px solid var(--se-action-secondary-border)',
    hoverBg: 'var(--se-action-secondary-hover)',
    hoverColor: 'var(--se-action-secondary-text-hover)'
  },
  tertiary: {
    background: 'transparent',
    color: 'var(--se-action-secondary-text)',
    border: '1.5px solid transparent',
    hoverBg: 'var(--se-action-secondary-hover)',
    hoverColor: 'var(--se-action-secondary-text-hover)'
  },
  ghost: {
    background: 'var(--se-base-1)',
    color: 'var(--se-text-primary)',
    border: '1.5px solid transparent',
    hoverBg: 'var(--se-base-1-hover)'
  },
  danger: {
    background: 'var(--se-action-danger)',
    color: 'var(--se-action-danger-text)',
    border: '1.5px solid transparent',
    hoverBg: 'var(--se-action-danger-hover)'
  },
  warning: {
    background: 'var(--se-action-warning)',
    color: 'var(--se-action-warning-text)',
    border: '1.5px solid transparent',
    hoverBg: 'var(--se-action-warning-hover)'
  }
};
const SIZES = {
  sm: {
    paddingBlock: 4,
    fontSize: 14
  },
  md: {
    paddingBlock: 8,
    fontSize: 14
  },
  lg: {
    paddingBlock: 12,
    fontSize: 14
  }
};
function Button({
  variant = 'primary',
  size = 'md',
  disabled = false,
  children,
  onClick,
  type = 'button',
  style
}) {
  const [hover, setHover] = React.useState(false);
  const v = VARIANTS[variant] || VARIANTS.primary;
  const s = SIZES[size] || SIZES.md;
  return /*#__PURE__*/React.createElement("button", {
    type: type,
    disabled: disabled,
    onClick: onClick,
    onMouseEnter: () => setHover(true),
    onMouseLeave: () => setHover(false),
    style: {
      fontFamily: 'var(--se-font-family)',
      fontWeight: 600,
      fontSize: s.fontSize,
      lineHeight: '16px',
      paddingBlock: s.paddingBlock,
      paddingInline: 16,
      borderRadius: 'var(--se-radius-1)',
      border: v.border,
      background: hover && !disabled ? v.hoverBg : v.background,
      color: hover && !disabled && v.hoverColor ? v.hoverColor : v.color,
      borderColor: variant === 'secondary' ? hover && !disabled ? 'var(--se-action-secondary-border-hover)' : undefined : undefined,
      cursor: disabled ? 'not-allowed' : 'pointer',
      opacity: disabled ? 'var(--se-action-disabled-opacity)' : 1,
      display: 'inline-flex',
      alignItems: 'center',
      justifyContent: 'center',
      gap: 6,
      userSelect: 'none',
      transition: 'background-color .15s ease-in-out, color .15s ease-in-out, border-color .15s ease-in-out',
      ...style
    }
  }, children);
}
Object.assign(__ds_scope, { Button });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/buttons/Button.jsx", error: String((e && e.message) || e) }); }

// components/core/Avatar.jsx
try { (() => {
const COLORS = ['#006b80', '#a733bc', '#1c703f', '#a84100', '#1e5299', '#a60823'];
function hash(str) {
  let h = 0;
  for (let i = 0; i < str.length; i++) h = h * 31 + str.charCodeAt(i) >>> 0;
  return h;
}
function Avatar({
  name = '',
  size = 36,
  imageUrl
}) {
  const initials = name.split(' ').slice(0, 2).map(p => p[0]).join('').toUpperCase();
  const bg = COLORS[hash(name) % COLORS.length];
  return /*#__PURE__*/React.createElement("div", {
    style: {
      width: size,
      height: size,
      borderRadius: '50%',
      background: imageUrl ? undefined : bg,
      backgroundImage: imageUrl ? `url(${imageUrl})` : undefined,
      backgroundSize: 'cover',
      backgroundPosition: 'center',
      color: '#fff',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      fontFamily: 'var(--se-font-family)',
      fontWeight: 600,
      fontSize: size * 0.4,
      flex: 'none'
    }
  }, !imageUrl && initials);
}
Object.assign(__ds_scope, { Avatar });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/Avatar.jsx", error: String((e && e.message) || e) }); }

// components/core/Card.jsx
try { (() => {
function Card({
  heading,
  subHeading,
  accent,
  children,
  footer,
  style
}) {
  const accentColor = {
    primary: 'var(--se-ui-0)',
    info: 'var(--se-status-information)',
    success: 'var(--se-status-success)',
    warning: 'var(--se-status-warning)',
    danger: 'var(--se-status-danger)',
    critical: 'var(--se-status-critical)',
    inactive: 'var(--se-ui-4)'
  }[accent];
  return /*#__PURE__*/React.createElement("div", {
    style: {
      background: 'var(--se-base-1)',
      borderRadius: 'var(--se-radius-2)',
      borderInlineStart: accentColor ? '8px solid ' + accentColor : undefined,
      display: 'flex',
      flexDirection: 'column',
      fontFamily: 'var(--se-font-family)',
      overflow: 'hidden',
      ...style
    }
  }, heading ? /*#__PURE__*/React.createElement("div", {
    style: {
      padding: '12px 16px 0'
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      fontSize: 14,
      fontWeight: 700,
      color: 'var(--se-text-primary)'
    }
  }, heading), subHeading ? /*#__PURE__*/React.createElement("div", {
    style: {
      fontSize: 14,
      color: 'var(--se-text-secondary)',
      paddingTop: 8
    }
  }, subHeading) : null) : null, /*#__PURE__*/React.createElement("div", {
    style: {
      padding: 16,
      color: 'var(--se-text-primary)',
      fontSize: 14,
      flex: '1 1 auto'
    }
  }, children), footer ? /*#__PURE__*/React.createElement("div", {
    style: {
      padding: '12px 16px 16px'
    }
  }, footer) : null);
}
Object.assign(__ds_scope, { Card });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/Card.jsx", error: String((e && e.message) || e) }); }

// components/core/Icon.jsx
try { (() => {
function Icon({
  name,
  size = 20,
  color = 'currentColor',
  style,
  className
}) {
  const px = typeof size === 'number' ? `${size}px` : size;
  const data = typeof window !== 'undefined' && window.__SE_ICONS__ && window.__SE_ICONS__[name] || null;
  if (!data) {
    // Fallback: plain <img> (no recoloring) if icon data wasn't loaded for this name.
    return /*#__PURE__*/React.createElement("img", {
      src: `../../assets/icons/${name}.svg`,
      width: size,
      height: size,
      className: className,
      style: {
        display: 'inline-block',
        flex: 'none',
        ...style
      },
      alt: ""
    });
  }
  return /*#__PURE__*/React.createElement("svg", {
    className: className,
    viewBox: data.viewBox,
    width: px,
    height: px,
    style: {
      display: 'inline-block',
      flex: 'none',
      fill: color,
      ...style
    },
    dangerouslySetInnerHTML: {
      __html: data.inner
    }
  });
}
Object.assign(__ds_scope, { Icon });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/Icon.jsx", error: String((e && e.message) || e) }); }

// components/buttons/IconButton.jsx
try { (() => {
const VARIANTS = {
  ghost: {
    background: 'transparent',
    color: 'var(--se-ui-1)',
    hoverBg: 'var(--se-base-1-hover)'
  },
  filled: {
    background: 'var(--se-base-1)',
    color: 'var(--se-ui-1)',
    hoverBg: 'var(--se-base-1-hover)'
  },
  primary: {
    background: 'var(--se-action-primary)',
    color: 'var(--se-action-primary-text)',
    hoverBg: 'var(--se-action-primary-hover)'
  }
};
const SIZES = {
  sm: 28,
  md: 36,
  lg: 44
};
const ICON_SIZES = {
  sm: 16,
  md: 20,
  lg: 24
};
function IconButton({
  icon,
  variant = 'ghost',
  size = 'md',
  disabled,
  onClick,
  title,
  style
}) {
  const [hover, setHover] = React.useState(false);
  const v = VARIANTS[variant] || VARIANTS.ghost;
  const dim = SIZES[size] || SIZES.md;
  return /*#__PURE__*/React.createElement("button", {
    type: "button",
    title: title,
    "aria-label": title,
    disabled: disabled,
    onClick: onClick,
    onMouseEnter: () => setHover(true),
    onMouseLeave: () => setHover(false),
    style: {
      width: dim,
      height: dim,
      borderRadius: '50%',
      border: 'none',
      background: hover && !disabled ? v.hoverBg : v.background,
      color: v.color,
      display: 'inline-flex',
      alignItems: 'center',
      justifyContent: 'center',
      cursor: disabled ? 'not-allowed' : 'pointer',
      opacity: disabled ? 'var(--se-action-disabled-opacity)' : 1,
      flex: 'none',
      ...style
    }
  }, /*#__PURE__*/React.createElement(__ds_scope.Icon, {
    name: icon,
    size: ICON_SIZES[size] || 20,
    color: v.color
  }));
}
Object.assign(__ds_scope, { IconButton });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/buttons/IconButton.jsx", error: String((e && e.message) || e) }); }

// components/feedback/Badge.jsx
try { (() => {
const TYPES = {
  default: {
    bg: 'var(--se-base-0)',
    color: 'var(--se-text-primary)',
    outline: '1px solid var(--se-ui-4)'
  },
  primary: {
    bg: 'var(--se-ui-0)',
    color: 'var(--se-text-inverse)'
  },
  secondary: {
    bg: 'var(--se-ui-4)',
    color: 'var(--se-text-primary)'
  },
  info: {
    bg: 'var(--se-base-information)',
    color: 'var(--se-text-information)'
  },
  success: {
    bg: 'var(--se-base-success)',
    color: 'var(--se-text-success)'
  },
  caution: {
    bg: 'var(--se-base-caution)',
    color: 'var(--se-text-caution)'
  },
  warning: {
    bg: 'var(--se-base-warning)',
    color: 'var(--se-text-warning)'
  },
  danger: {
    bg: 'var(--se-base-danger)',
    color: 'var(--se-text-danger)'
  },
  critical: {
    bg: 'var(--se-base-critical)',
    color: 'var(--se-text-critical)'
  },
  inverse: {
    bg: 'var(--se-ui-1)',
    color: 'var(--se-text-inverse)'
  }
};
function Badge({
  type = 'default',
  icon,
  children
}) {
  const t = TYPES[type] || TYPES.default;
  return /*#__PURE__*/React.createElement("span", {
    style: {
      display: 'inline-flex',
      alignItems: 'center',
      gap: 4,
      fontFamily: 'var(--se-font-family)',
      fontSize: 14,
      lineHeight: '20px',
      fontWeight: 400,
      color: t.color,
      background: t.bg,
      outline: t.outline,
      outlineOffset: -1,
      borderRadius: 12,
      padding: icon ? '2px 8px 2px 6px' : '2px 8px',
      whiteSpace: 'nowrap'
    }
  }, icon ? /*#__PURE__*/React.createElement(__ds_scope.Icon, {
    name: icon,
    size: 14,
    color: t.color
  }) : null, children);
}
Object.assign(__ds_scope, { Badge });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/feedback/Badge.jsx", error: String((e && e.message) || e) }); }

// components/feedback/EmptyState.jsx
try { (() => {
function EmptyState({
  icon = 'document',
  title,
  explanation,
  actionLabel,
  onAction
}) {
  return /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      textAlign: 'center',
      gap: 8,
      padding: '48px 24px',
      fontFamily: 'var(--se-font-family)'
    }
  }, /*#__PURE__*/React.createElement(__ds_scope.Icon, {
    name: icon,
    size: 48,
    color: "var(--se-ui-3)"
  }), /*#__PURE__*/React.createElement("div", {
    style: {
      fontSize: 16,
      fontWeight: 600,
      color: 'var(--se-text-primary)'
    }
  }, title), explanation ? /*#__PURE__*/React.createElement("div", {
    style: {
      fontSize: 14,
      color: 'var(--se-text-secondary)',
      maxWidth: 320
    }
  }, explanation) : null, actionLabel ? /*#__PURE__*/React.createElement("div", {
    style: {
      marginTop: 8
    }
  }, /*#__PURE__*/React.createElement(__ds_scope.Button, {
    variant: "secondary",
    onClick: onAction
  }, actionLabel)) : null);
}
Object.assign(__ds_scope, { EmptyState });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/feedback/EmptyState.jsx", error: String((e && e.message) || e) }); }

// components/feedback/StatusDot.jsx
try { (() => {
const TYPES = {
  information: 'var(--se-status-information)',
  success: 'var(--se-status-success)',
  caution: 'var(--se-status-caution)',
  warning: 'var(--se-status-warning)',
  danger: 'var(--se-status-danger)',
  critical: 'var(--se-status-critical)'
};
function StatusDot({
  status = 'information',
  size = 10,
  label
}) {
  return /*#__PURE__*/React.createElement("span", {
    style: {
      display: 'inline-flex',
      alignItems: 'center',
      gap: 8,
      fontFamily: 'var(--se-font-family)',
      fontSize: 14,
      color: 'var(--se-text-primary)'
    }
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      width: size,
      height: size,
      borderRadius: '50%',
      background: TYPES[status] || TYPES.information,
      flex: 'none'
    }
  }), label);
}
Object.assign(__ds_scope, { StatusDot });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/feedback/StatusDot.jsx", error: String((e && e.message) || e) }); }

// components/forms/Checkbox.jsx
try { (() => {
function Checkbox({
  label,
  checked,
  onChange,
  disabled,
  indeterminate
}) {
  const ref = React.useRef(null);
  React.useEffect(() => {
    if (ref.current) ref.current.indeterminate = !!indeterminate;
  }, [indeterminate]);
  return /*#__PURE__*/React.createElement("label", {
    style: {
      display: 'inline-flex',
      alignItems: 'center',
      gap: 8,
      fontFamily: 'var(--se-font-family)',
      fontSize: 14,
      color: disabled ? 'var(--se-text-disabled)' : 'var(--se-text-primary)',
      cursor: disabled ? 'not-allowed' : 'pointer'
    }
  }, /*#__PURE__*/React.createElement("input", {
    ref: ref,
    type: "checkbox",
    checked: checked,
    disabled: disabled,
    onChange: onChange,
    style: {
      width: 18,
      height: 18,
      accentColor: 'var(--se-ui-0)',
      margin: 0
    }
  }), label);
}
Object.assign(__ds_scope, { Checkbox });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/forms/Checkbox.jsx", error: String((e && e.message) || e) }); }

// components/forms/Select.jsx
try { (() => {
function Select({
  label,
  value,
  onChange,
  options = [],
  disabled
}) {
  return /*#__PURE__*/React.createElement("div", {
    style: {
      fontFamily: 'var(--se-font-family)',
      display: 'flex',
      flexDirection: 'column',
      gap: 4
    }
  }, label ? /*#__PURE__*/React.createElement("label", {
    style: {
      fontSize: 14,
      color: 'var(--se-text-secondary)'
    }
  }, label) : null, /*#__PURE__*/React.createElement("div", {
    style: {
      position: 'relative'
    }
  }, /*#__PURE__*/React.createElement("select", {
    value: value,
    disabled: disabled,
    onChange: onChange,
    style: {
      appearance: 'none',
      fontFamily: 'var(--se-font-family)',
      fontSize: 14,
      color: disabled ? 'var(--se-text-disabled)' : 'var(--se-text-primary)',
      background: 'var(--se-base-1)',
      border: '1px solid var(--se-ui-2)',
      borderRadius: 'var(--se-radius-1)',
      padding: '8px 32px 8px 8px',
      width: '100%',
      boxSizing: 'border-box'
    }
  }, options.map(o => /*#__PURE__*/React.createElement("option", {
    key: o.value,
    value: o.value
  }, o.label))), /*#__PURE__*/React.createElement(__ds_scope.Icon, {
    name: "down-1",
    size: 16,
    color: "var(--se-ui-2)",
    style: {
      position: 'absolute',
      right: 8,
      top: '50%',
      transform: 'translateY(-50%)',
      pointerEvents: 'none'
    }
  })));
}
Object.assign(__ds_scope, { Select });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/forms/Select.jsx", error: String((e && e.message) || e) }); }

// components/forms/Switch.jsx
try { (() => {
function Switch({
  label,
  checked,
  onChange,
  disabled
}) {
  return /*#__PURE__*/React.createElement("label", {
    style: {
      display: 'inline-flex',
      alignItems: 'center',
      gap: 8,
      fontFamily: 'var(--se-font-family)',
      fontSize: 14,
      color: disabled ? 'var(--se-text-disabled)' : 'var(--se-text-primary)',
      cursor: disabled ? 'not-allowed' : 'pointer'
    }
  }, /*#__PURE__*/React.createElement("span", {
    onClick: () => !disabled && onChange && onChange(!checked),
    style: {
      width: 36,
      height: 20,
      borderRadius: 999,
      background: checked ? 'var(--se-ui-0)' : 'var(--se-ui-3)',
      position: 'relative',
      transition: 'background-color .15s ease-in-out',
      opacity: disabled ? 'var(--se-action-disabled-opacity)' : 1,
      flex: 'none'
    }
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      position: 'absolute',
      top: 2,
      left: checked ? 18 : 2,
      width: 16,
      height: 16,
      borderRadius: '50%',
      background: '#fff',
      transition: 'left .15s ease-in-out',
      boxShadow: '0 1px 2px rgba(0,0,0,.24)'
    }
  })), label);
}
Object.assign(__ds_scope, { Switch });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/forms/Switch.jsx", error: String((e && e.message) || e) }); }

// components/forms/TextInput.jsx
try { (() => {
function TextInput({
  label,
  placeholder,
  value,
  onChange,
  disabled,
  invalid,
  hint,
  size = 'md'
}) {
  const [focused, setFocused] = React.useState(false);
  const borderColor = invalid ? 'var(--se-status-danger)' : focused ? 'var(--se-ui-1)' : 'var(--se-ui-2)';
  return /*#__PURE__*/React.createElement("div", {
    style: {
      fontFamily: 'var(--se-font-family)',
      display: 'flex',
      flexDirection: 'column',
      gap: 4,
      width: '100%'
    }
  }, label ? /*#__PURE__*/React.createElement("label", {
    style: {
      fontSize: 14,
      color: 'var(--se-text-secondary)'
    }
  }, label) : null, /*#__PURE__*/React.createElement("input", {
    placeholder: placeholder,
    value: value,
    disabled: disabled,
    onChange: onChange,
    onFocus: () => setFocused(true),
    onBlur: () => setFocused(false),
    style: {
      fontFamily: 'var(--se-font-family)',
      fontSize: 14,
      lineHeight: '16px',
      color: disabled ? 'var(--se-text-disabled)' : 'var(--se-text-primary)',
      background: 'var(--se-base-1)',
      border: '1px solid ' + (disabled ? 'var(--se-ui-4)' : borderColor),
      borderRadius: 'var(--se-radius-1)',
      padding: size === 'sm' ? '6px 8px' : '8px',
      outline: 'none',
      boxShadow: focused && !invalid ? '0 0 0 1px var(--se-ui-1)' : 'none',
      width: '100%',
      boxSizing: 'border-box'
    }
  }), hint ? /*#__PURE__*/React.createElement("span", {
    style: {
      fontSize: 12,
      color: invalid ? 'var(--se-text-danger)' : 'var(--se-text-secondary)'
    }
  }, hint) : null);
}
Object.assign(__ds_scope, { TextInput });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/forms/TextInput.jsx", error: String((e && e.message) || e) }); }

// components/navigation/Tabs.jsx
try { (() => {
function Tabs({
  tabs = [],
  value,
  onChange
}) {
  return /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      borderBottom: '1px solid var(--se-ui-4)',
      fontFamily: 'var(--se-font-family)'
    }
  }, tabs.map(t => {
    const active = t.value === value;
    return /*#__PURE__*/React.createElement("button", {
      key: t.value,
      onClick: () => onChange && onChange(t.value),
      style: {
        background: 'transparent',
        border: 'none',
        borderBottom: '2px solid ' + (active ? 'var(--se-action-secondary-text-hover)' : 'transparent'),
        color: active ? 'var(--se-action-secondary-text-hover)' : 'var(--se-text-primary)',
        fontSize: 16,
        fontWeight: 600,
        padding: '10px 24px',
        cursor: 'pointer',
        marginBottom: -1
      }
    }, t.label);
  }));
}
Object.assign(__ds_scope, { Tabs });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/navigation/Tabs.jsx", error: String((e && e.message) || e) }); }

// ui_kits/asset-monitoring/AppHeader.jsx
try { (() => {
function AppHeader({
  appName,
  active,
  onNavigate
}) {
  const {
    Icon,
    IconButton,
    Avatar
  } = window.SiemensEnergyDesignSystem_70efdf;
  const navItems = ['Overview', 'Assets', 'Alarms', 'Reports'];
  return /*#__PURE__*/React.createElement("header", {
    style: {
      height: 56,
      display: 'flex',
      alignItems: 'center',
      gap: 24,
      padding: '0 16px',
      background: 'var(--se-base-1)',
      borderBottom: '1px solid var(--se-ui-4)',
      fontFamily: 'var(--se-font-family)',
      flex: 'none'
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      alignItems: 'center',
      gap: 8,
      fontWeight: 700,
      fontSize: 16,
      color: 'var(--se-ui-1)'
    }
  }, /*#__PURE__*/React.createElement(Icon, {
    name: "dashboard",
    size: 24,
    color: "var(--se-ui-0)"
  }), appName), /*#__PURE__*/React.createElement("nav", {
    style: {
      display: 'flex',
      gap: 4,
      flex: '1 1 auto'
    }
  }, navItems.map(n => {
    const isActive = n === active;
    return /*#__PURE__*/React.createElement("button", {
      key: n,
      onClick: () => onNavigate && onNavigate(n),
      style: {
        background: 'transparent',
        border: 'none',
        borderBottom: '2px solid ' + (isActive ? 'var(--se-action-secondary-text-hover)' : 'transparent'),
        color: isActive ? 'var(--se-action-secondary-text-hover)' : 'var(--se-text-primary)',
        fontSize: 14,
        fontWeight: 600,
        padding: '0 4px',
        height: 55,
        cursor: 'pointer',
        fontFamily: 'var(--se-font-family)'
      }
    }, n);
  })), /*#__PURE__*/React.createElement(IconButton, {
    icon: "search",
    title: "Search"
  }), /*#__PURE__*/React.createElement(IconButton, {
    icon: "alarm-filled",
    title: "Alarms"
  }), /*#__PURE__*/React.createElement(IconButton, {
    icon: "settings",
    title: "Settings"
  }), /*#__PURE__*/React.createElement(Avatar, {
    name: "Ada Lovelace",
    size: 32
  }));
}
window.AppHeader = AppHeader;
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/asset-monitoring/AppHeader.jsx", error: String((e && e.message) || e) }); }

// ui_kits/asset-monitoring/AssetTable.jsx
try { (() => {
const ASSETS = [{
  name: 'Turbine A-12',
  site: 'Plant 3, Munich',
  status: 'success',
  label: 'Online',
  health: 98
}, {
  name: 'Compressor B-04',
  site: 'Plant 3, Munich',
  status: 'warning',
  label: 'Degraded',
  health: 71
}, {
  name: 'Generator C-01',
  site: 'Plant 1, Erlangen',
  status: 'danger',
  label: 'Offline',
  health: 0
}, {
  name: 'Pump D-22',
  site: 'Plant 2, Berlin',
  status: 'success',
  label: 'Online',
  health: 100
}, {
  name: 'Transformer E-09',
  site: 'Plant 1, Erlangen',
  status: 'success',
  label: 'Online',
  health: 95
}];
window.ASSETS = ASSETS;
function AssetTable({
  onSelect
}) {
  const {
    StatusDot
  } = window.SiemensEnergyDesignSystem_70efdf;
  return /*#__PURE__*/React.createElement("div", {
    style: {
      background: 'var(--se-base-1)',
      borderRadius: 'var(--se-radius-2)',
      overflow: 'hidden',
      fontFamily: 'var(--se-font-family)'
    }
  }, /*#__PURE__*/React.createElement("table", {
    style: {
      width: '100%',
      borderCollapse: 'collapse',
      fontSize: 14
    }
  }, /*#__PURE__*/React.createElement("thead", null, /*#__PURE__*/React.createElement("tr", {
    style: {
      borderBottom: '1px solid var(--se-ui-4)',
      textAlign: 'left'
    }
  }, ['Asset', 'Site', 'Status', 'Health'].map(h => /*#__PURE__*/React.createElement("th", {
    key: h,
    style: {
      padding: '12px 16px',
      color: 'var(--se-text-secondary)',
      fontWeight: 600,
      fontSize: 12
    }
  }, h)))), /*#__PURE__*/React.createElement("tbody", null, ASSETS.map(a => /*#__PURE__*/React.createElement("tr", {
    key: a.name,
    onClick: () => onSelect && onSelect(a),
    style: {
      borderBottom: '1px solid var(--se-ui-4)',
      cursor: onSelect ? 'pointer' : 'default'
    },
    onMouseEnter: e => e.currentTarget.style.background = 'var(--se-base-1-hover)',
    onMouseLeave: e => e.currentTarget.style.background = 'transparent'
  }, /*#__PURE__*/React.createElement("td", {
    style: {
      padding: '12px 16px',
      color: 'var(--se-text-primary)',
      fontWeight: 600
    }
  }, a.name), /*#__PURE__*/React.createElement("td", {
    style: {
      padding: '12px 16px',
      color: 'var(--se-text-secondary)'
    }
  }, a.site), /*#__PURE__*/React.createElement("td", {
    style: {
      padding: '12px 16px'
    }
  }, /*#__PURE__*/React.createElement(StatusDot, {
    status: a.status,
    label: a.label
  })), /*#__PURE__*/React.createElement("td", {
    style: {
      padding: '12px 16px',
      color: 'var(--se-text-secondary)'
    }
  }, a.health, "%"))))));
}
window.AssetTable = AssetTable;
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/asset-monitoring/AssetTable.jsx", error: String((e && e.message) || e) }); }

// ui_kits/asset-monitoring/Screens.jsx
try { (() => {
function OverviewScreen() {
  const {
    Card,
    Badge
  } = window.SiemensEnergyDesignSystem_70efdf;
  return /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      flexDirection: 'column',
      gap: 16
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'grid',
      gridTemplateColumns: 'repeat(4, 1fr)',
      gap: 16
    }
  }, /*#__PURE__*/React.createElement(Card, {
    heading: "Assets online",
    style: {
      minHeight: 90
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      fontSize: 28,
      fontWeight: 700,
      color: 'var(--se-text-primary)'
    }
  }, "142"), /*#__PURE__*/React.createElement(Badge, {
    type: "success"
  }, "+3 today")), /*#__PURE__*/React.createElement(Card, {
    heading: "Open alarms",
    accent: "danger",
    style: {
      minHeight: 90
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      fontSize: 28,
      fontWeight: 700,
      color: 'var(--se-text-primary)'
    }
  }, "7"), /*#__PURE__*/React.createElement(Badge, {
    type: "danger"
  }, "2 critical")), /*#__PURE__*/React.createElement(Card, {
    heading: "Avg. health",
    style: {
      minHeight: 90
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      fontSize: 28,
      fontWeight: 700,
      color: 'var(--se-text-primary)'
    }
  }, "93%"), /*#__PURE__*/React.createElement(Badge, {
    type: "info"
  }, "Stable")), /*#__PURE__*/React.createElement(Card, {
    heading: "Maintenance due",
    style: {
      minHeight: 90
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      fontSize: 28,
      fontWeight: 700,
      color: 'var(--se-text-primary)'
    }
  }, "4"), /*#__PURE__*/React.createElement(Badge, {
    type: "caution"
  }, "This week"))), /*#__PURE__*/React.createElement("div", {
    style: {
      fontSize: 16,
      fontWeight: 600,
      color: 'var(--se-text-primary)'
    }
  }, "Recent asset activity"), /*#__PURE__*/React.createElement(window.AssetTable, null));
}
window.OverviewScreen = OverviewScreen;
function AssetsScreen({
  onSelect
}) {
  return /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      flexDirection: 'column',
      gap: 16
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      justifyContent: 'space-between',
      alignItems: 'center'
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      fontSize: 20,
      fontWeight: 600,
      color: 'var(--se-text-primary)'
    }
  }, "Assets"), /*#__PURE__*/React.createElement(window.SiemensEnergyDesignSystem_70efdf.Button, {
    variant: "primary"
  }, "Add asset")), /*#__PURE__*/React.createElement(window.AssetTable, {
    onSelect: onSelect
  }));
}
window.AssetsScreen = AssetsScreen;
function AssetDetailScreen({
  asset,
  onBack
}) {
  const {
    Button,
    Badge,
    Tabs,
    TextInput,
    Select
  } = window.SiemensEnergyDesignSystem_70efdf;
  const [tab, setTab] = React.useState('overview');
  const statusType = asset.status;
  return /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      flexDirection: 'column',
      gap: 16
    }
  }, /*#__PURE__*/React.createElement(Button, {
    variant: "tertiary",
    onClick: onBack,
    style: {
      alignSelf: 'flex-start',
      paddingInline: 0
    }
  }, "\u2190 Back to assets"), /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      justifyContent: 'space-between',
      alignItems: 'center'
    }
  }, /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement("div", {
    style: {
      fontSize: 24,
      fontWeight: 400,
      color: 'var(--se-text-primary)'
    }
  }, asset.name), /*#__PURE__*/React.createElement("div", {
    style: {
      fontSize: 14,
      color: 'var(--se-text-secondary)'
    }
  }, asset.site)), /*#__PURE__*/React.createElement(Badge, {
    type: statusType
  }, asset.label)), /*#__PURE__*/React.createElement(Tabs, {
    value: tab,
    onChange: setTab,
    tabs: [{
      value: 'overview',
      label: 'Overview'
    }, {
      value: 'settings',
      label: 'Settings'
    }]
  }), tab === 'overview' ? /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'grid',
      gridTemplateColumns: 'repeat(3,1fr)',
      gap: 16
    }
  }, /*#__PURE__*/React.createElement(window.SiemensEnergyDesignSystem_70efdf.Card, {
    heading: "Health"
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      fontSize: 28,
      fontWeight: 700
    }
  }, asset.health, "%")), /*#__PURE__*/React.createElement(window.SiemensEnergyDesignSystem_70efdf.Card, {
    heading: "Uptime (30d)"
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      fontSize: 28,
      fontWeight: 700
    }
  }, asset.health > 0 ? '99.2%' : '0%')), /*#__PURE__*/React.createElement(window.SiemensEnergyDesignSystem_70efdf.Card, {
    heading: "Last maintenance"
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      fontSize: 16,
      color: 'var(--se-text-secondary)'
    }
  }, "12 May 2026"))) : /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      flexDirection: 'column',
      gap: 12,
      maxWidth: 360
    }
  }, /*#__PURE__*/React.createElement(TextInput, {
    label: "Asset name",
    value: asset.name,
    onChange: () => {}
  }), /*#__PURE__*/React.createElement(Select, {
    label: "Site",
    value: "1",
    onChange: () => {},
    options: [{
      value: '1',
      label: asset.site
    }]
  }), /*#__PURE__*/React.createElement(Button, {
    variant: "primary",
    style: {
      alignSelf: 'flex-start'
    }
  }, "Save changes")));
}
window.AssetDetailScreen = AssetDetailScreen;
function AlarmsScreen() {
  const {
    Badge
  } = window.SiemensEnergyDesignSystem_70efdf;
  const alarms = [{
    asset: 'Generator C-01',
    message: 'Overpressure detected',
    severity: 'critical',
    time: '08:12'
  }, {
    asset: 'Compressor B-04',
    message: 'Vibration threshold exceeded',
    severity: 'warning',
    time: '07:45'
  }, {
    asset: 'Turbine A-12',
    message: 'Scheduled inspection due',
    severity: 'info',
    time: 'Yesterday'
  }];
  const badgeType = {
    critical: 'critical',
    warning: 'warning',
    info: 'info'
  };
  return /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      flexDirection: 'column',
      gap: 16
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      fontSize: 20,
      fontWeight: 600,
      color: 'var(--se-text-primary)'
    }
  }, "Alarms"), /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      flexDirection: 'column',
      gap: 8
    }
  }, alarms.map((a, i) => /*#__PURE__*/React.createElement("div", {
    key: i,
    style: {
      display: 'flex',
      alignItems: 'center',
      gap: 12,
      background: 'var(--se-base-1)',
      borderRadius: 'var(--se-radius-2)',
      padding: '12px 16px'
    }
  }, /*#__PURE__*/React.createElement(Badge, {
    type: badgeType[a.severity]
  }, a.severity), /*#__PURE__*/React.createElement("div", {
    style: {
      flex: '1 1 auto'
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      fontSize: 14,
      fontWeight: 600,
      color: 'var(--se-text-primary)'
    }
  }, a.asset), /*#__PURE__*/React.createElement("div", {
    style: {
      fontSize: 13,
      color: 'var(--se-text-secondary)'
    }
  }, a.message)), /*#__PURE__*/React.createElement("div", {
    style: {
      fontSize: 12,
      color: 'var(--se-text-secondary)'
    }
  }, a.time)))));
}
window.AlarmsScreen = AlarmsScreen;
function ReportsScreen() {
  const {
    EmptyState
  } = window.SiemensEnergyDesignSystem_70efdf;
  return /*#__PURE__*/React.createElement(EmptyState, {
    icon: "document",
    title: "No reports yet",
    explanation: "Generate a report to see it here",
    actionLabel: "Create report"
  });
}
window.ReportsScreen = ReportsScreen;
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/asset-monitoring/Screens.jsx", error: String((e && e.message) || e) }); }

__ds_ns.Button = __ds_scope.Button;

__ds_ns.IconButton = __ds_scope.IconButton;

__ds_ns.Avatar = __ds_scope.Avatar;

__ds_ns.Card = __ds_scope.Card;

__ds_ns.Icon = __ds_scope.Icon;

__ds_ns.Badge = __ds_scope.Badge;

__ds_ns.EmptyState = __ds_scope.EmptyState;

__ds_ns.StatusDot = __ds_scope.StatusDot;

__ds_ns.Checkbox = __ds_scope.Checkbox;

__ds_ns.Select = __ds_scope.Select;

__ds_ns.Switch = __ds_scope.Switch;

__ds_ns.TextInput = __ds_scope.TextInput;

__ds_ns.Tabs = __ds_scope.Tabs;

})();
