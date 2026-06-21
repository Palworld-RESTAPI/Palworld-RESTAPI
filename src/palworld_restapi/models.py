from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True, frozen=True)
class ServerInfo:
    version: str
    servername: str
    description: str
    worldguid: str
    raw: dict[str, Any] = field(repr=False, hash=False, compare=False)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "ServerInfo":
        return cls(
            version=data.get("version", ""),
            servername=data.get("servername", ""),
            description=data.get("description", ""),
            worldguid=data.get("worldguid", ""),
            raw=data,
        )


@dataclass(slots=True, frozen=True)
class PlayerInfo:
    name: str
    accountName: str
    playerId: str
    userId: str
    ip: str
    ping: float
    location_x: float
    location_y: float
    level: int
    building_count: int
    raw: dict[str, Any] = field(repr=False, hash=False, compare=False)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "PlayerInfo":
        return cls(
            name=data.get("name", ""),
            accountName=data.get("accountName", ""),
            playerId=data.get("playerId", ""),
            userId=data.get("userId", ""),
            ip=data.get("ip", ""),
            ping=float(data.get("ping", 0.0)),
            location_x=float(data.get("location_x", 0.0)),
            location_y=float(data.get("location_y", 0.0)),
            level=int(data.get("level", 0)),
            building_count=int(data.get("building_count", 0)),
            raw=data,
        )


@dataclass(slots=True, frozen=True)
class PlayersResponse:
    players: list[PlayerInfo]
    raw: dict[str, Any] = field(repr=False, hash=False, compare=False)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "PlayersResponse":
        return cls(
            players=[PlayerInfo.from_dict(p) for p in data.get("players", [])],
            raw=data,
        )


@dataclass(slots=True, frozen=True)
class ServerMetrics:
    serverfps: int
    currentplayernum: int
    serverframetime: float
    maxplayernum: int
    uptime: int
    basecampnum: int
    days: int
    raw: dict[str, Any] = field(repr=False, hash=False, compare=False)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "ServerMetrics":
        return cls(
            serverfps=int(data.get("serverfps", 0)),
            currentplayernum=int(data.get("currentplayernum", 0)),
            serverframetime=float(data.get("serverframetime", 0.0)),
            maxplayernum=int(data.get("maxplayernum", 0)),
            uptime=int(data.get("uptime", 0)),
            basecampnum=int(data.get("basecampnum", 0)),
            days=int(data.get("days", 0)),
            raw=data,
        )


@dataclass(slots=True, frozen=True)
class ServerSettings:
    Difficulty: str
    DayTimeSpeedRate: float
    NightTimeSpeedRate: float
    ExpRate: float
    PalCaptureRate: float
    PalSpawnNumRate: float
    PalDamageRateAttack: float
    PalDamageRateDefense: float
    PlayerDamageRateAttack: float
    PlayerDamageRateDefense: float
    PlayerStomachDecreaceRate: float
    PlayerStaminaDecreaceRate: float
    PlayerAutoHPRegeneRate: float
    PlayerAutoHpRegeneRateInSleep: float
    PalStomachDecreaceRate: float
    PalStaminaDecreaceRate: float
    PalAutoHPRegeneRate: float
    PalAutoHpRegeneRateInSleep: float
    BuildObjectDamageRate: float
    BuildObjectDeteriorationDamageRate: float
    CollectionDropRate: float
    CollectionObjectHpRate: float
    CollectionObjectRespawnSpeedRate: float
    EnemyDropItemRate: float
    DeathPenalty: str
    bEnablePlayerToPlayerDamage: bool
    bEnableFriendlyFire: bool
    bEnableInvaderEnemy: bool
    bActiveUNKO: bool
    bEnableAimAssistPad: bool
    bEnableAimAssistKeyboard: bool
    DropItemMaxNum: int
    DropItemMaxNum_UNKO: int
    BaseCampMaxNum: int
    BaseCampWorkerMaxNum: int
    DropItemAliveMaxHours: float
    bAutoResetGuildNoOnlinePlayers: bool
    AutoResetGuildTimeNoOnlinePlayers: float
    GuildPlayerMaxNum: int
    PalEggDefaultHatchingTime: float
    WorkSpeedRate: float
    bIsMultiplay: bool
    bIsPvP: bool
    bCanPickupOtherGuildDeathPenaltyDrop: bool
    bEnableNonLoginPenalty: bool
    bEnableFastTravel: bool
    bIsStartLocationSelectByMap: bool
    bExistPlayerAfterLogout: bool
    bEnableDefenseOtherGuildPlayer: bool
    CoopPlayerMaxNum: int
    ServerPlayerMaxNum: int
    ServerName: str
    ServerDescription: str
    PublicPort: int
    PublicIP: str
    RCONEnabled: bool
    RCONPort: int
    Region: str
    bUseAuth: bool
    BanListURL: str
    RESTAPIEnabled: bool
    RESTAPIPort: int
    bShowPlayerList: bool
    AllowConnectPlatform: str
    bIsUseBackupSaveData: bool
    LogFormatType: str
    raw: dict[str, Any] = field(repr=False, hash=False, compare=False)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "ServerSettings":
        return cls(
            Difficulty=data.get("Difficulty", ""),
            DayTimeSpeedRate=float(data.get("DayTimeSpeedRate", 0.0)),
            NightTimeSpeedRate=float(data.get("NightTimeSpeedRate", 0.0)),
            ExpRate=float(data.get("ExpRate", 0.0)),
            PalCaptureRate=float(data.get("PalCaptureRate", 0.0)),
            PalSpawnNumRate=float(data.get("PalSpawnNumRate", 0.0)),
            PalDamageRateAttack=float(data.get("PalDamageRateAttack", 0.0)),
            PalDamageRateDefense=float(data.get("PalDamageRateDefense", 0.0)),
            PlayerDamageRateAttack=float(data.get("PlayerDamageRateAttack", 0.0)),
            PlayerDamageRateDefense=float(data.get("PlayerDamageRateDefense", 0.0)),
            PlayerStomachDecreaceRate=float(data.get("PlayerStomachDecreaceRate", 0.0)),
            PlayerStaminaDecreaceRate=float(data.get("PlayerStaminaDecreaceRate", 0.0)),
            PlayerAutoHPRegeneRate=float(data.get("PlayerAutoHPRegeneRate", 0.0)),
            PlayerAutoHpRegeneRateInSleep=float(
                data.get("PlayerAutoHpRegeneRateInSleep", 0.0)
            ),
            PalStomachDecreaceRate=float(data.get("PalStomachDecreaceRate", 0.0)),
            PalStaminaDecreaceRate=float(data.get("PalStaminaDecreaceRate", 0.0)),
            PalAutoHPRegeneRate=float(data.get("PalAutoHPRegeneRate", 0.0)),
            PalAutoHpRegeneRateInSleep=float(
                data.get("PalAutoHpRegeneRateInSleep", 0.0)
            ),
            BuildObjectDamageRate=float(data.get("BuildObjectDamageRate", 0.0)),
            BuildObjectDeteriorationDamageRate=float(
                data.get("BuildObjectDeteriorationDamageRate", 0.0)
            ),
            CollectionDropRate=float(data.get("CollectionDropRate", 0.0)),
            CollectionObjectHpRate=float(data.get("CollectionObjectHpRate", 0.0)),
            CollectionObjectRespawnSpeedRate=float(
                data.get("CollectionObjectRespawnSpeedRate", 0.0)
            ),
            EnemyDropItemRate=float(data.get("EnemyDropItemRate", 0.0)),
            DeathPenalty=data.get("DeathPenalty", ""),
            bEnablePlayerToPlayerDamage=bool(
                data.get("bEnablePlayerToPlayerDamage", False)
            ),
            bEnableFriendlyFire=bool(data.get("bEnableFriendlyFire", False)),
            bEnableInvaderEnemy=bool(data.get("bEnableInvaderEnemy", False)),
            bActiveUNKO=bool(data.get("bActiveUNKO", False)),
            bEnableAimAssistPad=bool(data.get("bEnableAimAssistPad", False)),
            bEnableAimAssistKeyboard=bool(data.get("bEnableAimAssistKeyboard", False)),
            DropItemMaxNum=int(data.get("DropItemMaxNum", 0)),
            DropItemMaxNum_UNKO=int(data.get("DropItemMaxNum_UNKO", 0)),
            BaseCampMaxNum=int(data.get("BaseCampMaxNum", 0)),
            BaseCampWorkerMaxNum=int(data.get("BaseCampWorkerMaxNum", 0)),
            DropItemAliveMaxHours=float(data.get("DropItemAliveMaxHours", 0.0)),
            bAutoResetGuildNoOnlinePlayers=bool(
                data.get("bAutoResetGuildNoOnlinePlayers", False)
            ),
            AutoResetGuildTimeNoOnlinePlayers=float(
                data.get("AutoResetGuildTimeNoOnlinePlayers", 0.0)
            ),
            GuildPlayerMaxNum=int(data.get("GuildPlayerMaxNum", 0)),
            PalEggDefaultHatchingTime=float(data.get("PalEggDefaultHatchingTime", 0.0)),
            WorkSpeedRate=float(data.get("WorkSpeedRate", 0.0)),
            bIsMultiplay=bool(data.get("bIsMultiplay", False)),
            bIsPvP=bool(data.get("bIsPvP", False)),
            bCanPickupOtherGuildDeathPenaltyDrop=bool(
                data.get("bCanPickupOtherGuildDeathPenaltyDrop", False)
            ),
            bEnableNonLoginPenalty=bool(data.get("bEnableNonLoginPenalty", False)),
            bEnableFastTravel=bool(data.get("bEnableFastTravel", False)),
            bIsStartLocationSelectByMap=bool(
                data.get("bIsStartLocationSelectByMap", False)
            ),
            bExistPlayerAfterLogout=bool(data.get("bExistPlayerAfterLogout", False)),
            bEnableDefenseOtherGuildPlayer=bool(
                data.get("bEnableDefenseOtherGuildPlayer", False)
            ),
            CoopPlayerMaxNum=int(data.get("CoopPlayerMaxNum", 0)),
            ServerPlayerMaxNum=int(data.get("ServerPlayerMaxNum", 0)),
            ServerName=data.get("ServerName", ""),
            ServerDescription=data.get("ServerDescription", ""),
            PublicPort=int(data.get("PublicPort", 0)),
            PublicIP=data.get("PublicIP", ""),
            RCONEnabled=bool(data.get("RCONEnabled", False)),
            RCONPort=int(data.get("RCONPort", 0)),
            Region=data.get("Region", ""),
            bUseAuth=bool(data.get("bUseAuth", False)),
            BanListURL=data.get("BanListURL", ""),
            RESTAPIEnabled=bool(data.get("RESTAPIEnabled", False)),
            RESTAPIPort=int(data.get("RESTAPIPort", 0)),
            bShowPlayerList=bool(data.get("bShowPlayerList", False)),
            AllowConnectPlatform=data.get("AllowConnectPlatform", ""),
            bIsUseBackupSaveData=bool(data.get("bIsUseBackupSaveData", False)),
            LogFormatType=data.get("LogFormatType", ""),
            raw=data,
        )
