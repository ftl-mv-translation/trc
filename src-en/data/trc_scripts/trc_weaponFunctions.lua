mods.trc = {}

-----------------------
-- UTILITY FUNCTIONS --
-----------------------

local userdata_table = mods.multiverse.userdata_table
local vter = mods.multiverse.vter

-----------
-- LOGIC --
-----------

mods.trc.burstSpriteFixes = {}
local burstSpriteFixes = mods.trc.burstSpriteFixes
burstSpriteFixes["TRC_CASH_GUN"] = true

script.on_internal_event(Defines.InternalEvents.PROJECTILE_FIRE, function(projectile, weapon)
    local isFake = projectile.death_animation.fScale == 0.25 
    if burstSpriteFixes[weapon and weapon.blueprint and weapon.blueprint.name] and not isFake then
        projectile:Initialize(Hyperspace.Blueprints:GetWeaponBlueprint(projectile.extend.name))
    end
end)

mods.trc.burstMultiBarrel = {}
local burstMultiBarrel = mods.trc.burstMultiBarrel
burstMultiBarrel["TRC_CASH_GUN"] = {
    barrelOffset = 7,
    barrelCount = 3
}

script.on_internal_event(Defines.InternalEvents.PROJECTILE_FIRE, function(projectile, weapon)
    local burstBarrelData = burstMultiBarrel[weapon and weapon.blueprint and weapon.blueprint.name]
    if burstBarrelData then
        local offset = (burstBarrelData.barrelCount - weapon.queuedProjectiles:size()%burstBarrelData.barrelCount - 1)*burstBarrelData.barrelOffset
        if weapon.mount.mirror then offset = -offset end
        if weapon.mount.rotate then
            projectile.position.y = projectile.position.y + offset
        else
            projectile.position.x = projectile.position.x + offset
        end
    end
end)

mods.trc.statChargers = {}
local statChargers = mods.trc.statChargers
statChargers["TRC_MAGNIFIER_1"] = {{stat = "iDamage"},{stat = "breachChance"},{stat = "fireChance"}}
statChargers["TRC_MAGNIFIER_2"] = {{stat = "iDamage"},{stat = "breachChance"},{stat = "fireChance"}}
statChargers["TRC_MAGNIFIER_PIERCE"] = {{stat = "iShieldPiercing"},{stat = "breachChance"}}
statChargers["TRC_MAGNIFIER_ION"] = {{stat = "iIonDamage"},{stat = "iStun"}}
script.on_internal_event(Defines.InternalEvents.PROJECTILE_FIRE, function(projectile, weapon)
    local statBoosts = statChargers[weapon and weapon.blueprint and weapon.blueprint.name]
    if statBoosts then
        local boost = weapon.queuedProjectiles:size() -- Gets how many projectiles are charged up (doesn't include the one that was already shot)
        weapon.queuedProjectiles:clear() -- Delete all other projectiles
        for _, statBoost in ipairs(statBoosts) do -- Apply all stat boosts
            if statBoost.calc then
                projectile.damage[statBoost.stat] = statBoost.calc(boost, projectile.damage[statBoost.stat])
            else
                projectile.damage[statBoost.stat] = boost + projectile.damage[statBoost.stat]
            end
        end
    end
end)

mods.trc.cooldownChargers = {}
local cooldownChargers = mods.trc.cooldownChargers
cooldownChargers["TRC_MAGNIFIER_1"] = 1.3
cooldownChargers["TRC_MAGNIFIER_2"] = 1.5
cooldownChargers["TRC_MAGNIFIER_PIERCE"] = 1.5
cooldownChargers["TRC_MAGNIFIER_ION"] = 1.2

script.on_internal_event(Defines.InternalEvents.SHIP_LOOP, function(ship)
    local weapons = ship and ship.weaponSystem and ship.weaponSystem.weapons
    if weapons then
        for weapon in vter(weapons) do
            if weapon.chargeLevel ~= 0 and weapon.chargeLevel < weapon.weaponVisual.iChargeLevels then
                local cdBoost = cooldownChargers[weapon and weapon.blueprint and weapon.blueprint.name]
                if cdBoost then
                    local cdLast = userdata_table(weapon, "mods.trc.weaponStuff").cdLast
                    if cdLast and weapon.cooldown.first > cdLast then
                        -- Calculate the new charge level from number of charges and charge level from last frame
                        local chargeUpdate = weapon.cooldown.first - cdLast
                        local chargeNew = weapon.cooldown.first - chargeUpdate + cdBoost^weapon.chargeLevel*chargeUpdate
                        
                        -- Apply the new charge level
                        if chargeNew >= weapon.cooldown.second then
                            weapon.chargeLevel = weapon.chargeLevel + 1
                            if weapon.chargeLevel == weapon.weaponVisual.iChargeLevels then
                                weapon.cooldown.first = weapon.cooldown.second
                            else
                                weapon.cooldown.first = 0
                            end
                        else
                            weapon.cooldown.first = chargeNew
                        end
                    end
                    userdata_table(weapon, "mods.trc.weaponStuff").cdLast = weapon.cooldown.first
                end
            end
        end
    end
end)

script.on_internal_event(Defines.InternalEvents.WEAPON_RENDERBOX, function(weapon, cooldown, maxCooldown, chargeString, damageString, shotLimitString)
    local chargerBoost = cooldownChargers[weapon and weapon.blueprint and weapon.blueprint.name]
    if chargerBoost then
        local first, second = chargeString:match("([%d%.]+)%s*/%s*([%d%.]+)")
        local boostLevel = math.min(weapon.chargeLevel, weapon.weaponVisual.iChargeLevels - 1)
        first = first / chargerBoost ^ boostLevel
        second = second / chargerBoost ^ boostLevel
        chargeString = string.format("%.1f / %.1f", first, second)
    end
    return Defines.Chain.CONTINUE, chargeString, damageString, shotLimitString
end)
