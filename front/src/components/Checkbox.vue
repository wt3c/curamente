<template>
<div class="checkbox__wrapper">
    <label :for="label">
        <input type="checkbox" :id="label">
        <span class="cbx">
            <svg width="12px" height="11px" viewBox="0 0 12 11">
                <polyline points="1 6.29411765 4.5 10 11 1"></polyline>
            </svg>
        </span>
        <span>{{ description }}</span>
    </label>
</div>
</template>

<script>
export default{
    name: "Checkbox",
    props: {
        description: String,
        label: String,
    }
}
</script>

<style>
.checkbox__wrapper .cbx {
    position: relative;
    display: block;
    float: left;
    width: 20px;
    height: 20px;
    border-radius: 6px;
    background-color: #c2c2c2;
    transition: all 0.15s ease;
    z-index: 0;
}

.checkbox__wrapper .cbx svg {
    position: absolute;
    top: 4px;
    left: 4px;
    fill: none;
    stroke-linecap: round;
    stroke-linejoin: round;
    stroke: #fff;
    stroke-width: 2;
    stroke-dasharray: 17;
    stroke-dashoffset: 17;
    transform: translate3d(0, 0, 0);
}
.checkbox__wrapper .cbx + span {
    margin-left: 6px;  
}
.checkbox__wrapper {
    user-select: none;
}
.checkbox__wrapper label {
    display: inline-flex;
    align-items: center;
    cursor: pointer;
}
.checkbox__wrapper input[type="checkbox"] {
    display: none;
    visibility: hidden;
}
.checkbox__wrapper input[type="checkbox"]:checked + .cbx {
    background-color: var(--dark-bg);
}
.checkbox__wrapper input[type="checkbox"]:checked + .cbx svg {
    stroke-dashoffset: 0;
    transition: all 0.15s ease;
}
</style>