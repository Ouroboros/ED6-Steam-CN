import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0001_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0001   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'map1'
    header.mapModel       = 'T0001.x'
    header.mapIndex       = 1
    header.bgm            = 0
    header.flags          = 0x0000
    header.entryFunction  = 0x0013
    header.importTable    = ['ED6_DT21/T0001._SN', 'ED6_DT21/T0001_1._SN', 'ED6_DT21/T0001_2._SN', 'ED6_DT21/T0001_3._SN', 'ED6_DT21/T0001_4._SN', 'ED6_DT21/T0001_5._SN', 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x00000000,
            dword_04        = 0x00000000,
            dword_08        = 0x00000000,
            word_0C         = 0x0004,
            word_0E         = 0x0005,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 2500,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 45,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 1,
            word_3A         = 1,
            preInitScena    = 0x0000,
            preInitFunction = 0x0001,
            initScena       = 0x0000,
            initFunction    = 0x0002,
        ),
    )

# id: 0x10000 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
        ('ED6_DT09/CH10000._CH', 'ED6_DT09/CH10000P._CP'),
        ('ED6_DT09/CH10001._CH', 'ED6_DT09/CH10001P._CP'),
    ]

# id: 0x10001 offset: 0xC2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '居民１',
            x                   = 4000,
            z                   = 0,
            y                   = -4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0001,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '呜喵',
            x                   = -4000,
            z                   = 0,
            y                   = -2000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0001,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '宝箱',
            x                   = -4000,
            z                   = 0,
            y                   = -4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0000,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '宝箱',
            x                   = -5000,
            z                   = 0,
            y                   = -6000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0000,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x142
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = 10000,
            z           = 0,
            y           = -4000,
            word_0C     = 0x0000,
            word_0E     = 0x0001,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x07D0,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x15E
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 10000,
            y           = 0,
            z           = -1000,
            range       = 11000,
            dword_10    = 0x000003E8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000B,
        ),
    )

# id: 0x10004 offset: 0x17E
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -2000,
            triggerZ            = 1000,
            triggerY            = 0,
            triggerRange        = 1000,
            actorX              = -2000,
            actorZ              = 1000,
            actorY              = 0,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -2000,
            triggerZ            = 1000,
            triggerY            = 0,
            triggerRange        = 2000,
            actorX              = -2000,
            actorZ              = 1000,
            actorY              = 0,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1C6
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x1C7
@scena.Code('func_01_1C7')
def func_01_1C7():
    Event(0, func_0B_CE5)
    OP_62(0x0009, 0xFFFFFDA8, 300, 0x80, 0x21, 0x000000FA, 0x00)
    ChrSetFlags(0x0009, 0x0006)

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetPos(0x0009, -4000, 1000, -2000, 0)

    ExecExpressionWithValue(
        0x0009,
        0x2A,
        (
            (Expr.PushLong, 0x7530),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x2B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x2C,
        (
            (Expr.PushLong, 0x15F90),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x2D,
        (
            (Expr.PushLong, 0x3E8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x2E,
        (
            (Expr.PushLong, 0x3E8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x2F,
        (
            (Expr.PushLong, 0x3E8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 0, 0x1000)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8B5',
    )

    SetScenaFlags(ScenaFlag(0x0200, 0, 0x1000))
    FormationDelMember(0x00, 0xFF)
    FormationAddMember(ChrTable['亚妮拉丝'], 0xF6, 0x00)
    FormationAddMember(ChrTable['克鲁茨'], 0xF7, 0x01)
    FormationAddMember(ChrTable['凯文神父'], 0xF8, 0x02)
    FormationAddMember(ChrTable['尤莉亚上尉'], 0xF9, 0x03)
    Call(2, 0x003A)
    ChrSetStatus(ChrTable['艾丝蒂尔'], 0x07, 4)
    ChrSetStatus(ChrTable['艾丝蒂尔'], 0x00, 3)
    ChrSetStatus(ChrTable['约修亚'], 0x07, 3)
    ChrSetStatus(ChrTable['艾丝蒂尔'], 0x07, 3)
    AddCraft(ChrTable['艾丝蒂尔'], CraftTable['助威'])
    AddCraft(ChrTable['艾丝蒂尔'], CraftTable['绞丝棍'])
    AddCraft(ChrTable['艾丝蒂尔'], CraftTable['金刚击'])
    AddCraft(ChrTable['艾丝蒂尔'], CraftTable['旋风轮'])
    AddCraft(ChrTable['艾丝蒂尔'], CraftTable['挑拨'])
    AddCraft(ChrTable['约修亚'], CraftTable['双连击'])
    AddCraft(ChrTable['约修亚'], CraftTable['绝影'])
    AddCraft(ChrTable['约修亚'], CraftTable['挑拨_00A4'])
    AddCraft(ChrTable['约修亚'], CraftTable['胧'])
    AddCraft(ChrTable['约修亚'], CraftTable['魔眼'])
    AddCraft(ChrTable['雪拉扎德'], CraftTable['风之鞭'])
    AddCraft(ChrTable['雪拉扎德'], CraftTable['拘束之鞭'])
    AddCraft(ChrTable['雪拉扎德'], CraftTable['天堂之吻'])
    AddCraft(ChrTable['奥利维尔'], CraftTable['快速狙击'])
    AddCraft(ChrTable['奥利维尔'], CraftTable['精准射击'])
    AddCraft(ChrTable['奥利维尔'], CraftTable['欢乐激发'])
    AddCraft(ChrTable['科洛丝'], CraftTable['斗魂'])
    AddCraft(ChrTable['科洛丝'], CraftTable['岚'])
    AddCraft(ChrTable['阿加特'], CraftTable['公牛之怒'])
    AddCraft(ChrTable['阿加特'], CraftTable['火焰碎击'])
    AddCraft(ChrTable['阿加特'], CraftTable['龙骑之刃'])
    AddCraft(ChrTable['阿加特'], CraftTable['螺旋之刃'])
    AddCraft(ChrTable['提妲'], CraftTable['烟幕弹'])
    AddCraft(ChrTable['提妲'], CraftTable['回复弹'])
    AddCraft(ChrTable['金'], CraftTable['龙神功'])
    AddCraft(ChrTable['金'], CraftTable['养命功'])
    AddCraft(ChrTable['金'], CraftTable['挑拨_00DC'])
    AddCraft(ChrTable['艾丝蒂尔'], CraftTable['连锁战技１(２人协力)'])
    AddCraft(ChrTable['约修亚'], CraftTable['连锁战技１(２人协力)'])
    AddCraft(ChrTable['雪拉扎德'], CraftTable['连锁战技１(２人协力)'])
    AddCraft(ChrTable['奥利维尔'], CraftTable['连锁战技１(２人协力)'])
    AddCraft(ChrTable['科洛丝'], CraftTable['连锁战技１(２人协力)'])
    AddCraft(ChrTable['阿加特'], CraftTable['连锁战技１(２人协力)'])
    AddCraft(ChrTable['提妲'], CraftTable['连锁战技１(２人协力)'])
    AddCraft(ChrTable['金'], CraftTable['连锁战技１(２人协力)'])
    AddSCraft(ChrTable['艾丝蒂尔'], CraftTable['烈波无双击'])
    AddSCraft(ChrTable['艾丝蒂尔'], CraftTable['樱花无双击'])
    AddSCraft(ChrTable['艾丝蒂尔'], CraftTable['奥义·太极轮'])
    AddSCraft(ChrTable['约修亚'], CraftTable['断骨剑'])
    AddSCraft(ChrTable['约修亚'], CraftTable['漆黑之牙'])
    AddSCraft(ChrTable['约修亚'], CraftTable['秘技·幻影奇袭'])
    AddSCraft(ChrTable['雪拉扎德'], CraftTable['女王之怒'])
    AddSCraft(ChrTable['雪拉扎德'], CraftTable['裁决塔罗'])
    AddSCraft(ChrTable['奥利维尔'], CraftTable['咆哮弹'])
    AddSCraft(ChrTable['奥利维尔'], CraftTable['乱心安魂曲'])
    AddSCraft(ChrTable['科洛丝'], CraftTable['光明之环'])
    AddSCraft(ChrTable['科洛丝'], CraftTable['圣星光旋'])
    AddSCraft(ChrTable['阿加特'], CraftTable['霸王疾风'])
    AddSCraft(ChrTable['阿加特'], CraftTable['终极裂斩'])
    AddSCraft(ChrTable['阿加特'], CraftTable['炎龙倒海'])
    AddSCraft(ChrTable['提妲'], CraftTable['炮射冲击'])
    AddSCraft(ChrTable['提妲'], CraftTable['卫星激光'])
    AddSCraft(ChrTable['金'], CraftTable['奥义·龙闪腿'])
    AddSCraft(ChrTable['金'], CraftTable['奥义·雷神掌'])
    AddSCraft(ChrTable['金'], CraftTable['奥义·泰山玄武靠'])
    AddSCraft(ChrTable['乔丝特'], CraftTable['山猫号'])
    AddCraft(ChrTable['凯文神父'], 0x0082)
    AddSCraft(ChrTable['凯文神父'], CraftTable['星杯领域'])
    AddItem(ItemTable['ＨＰ１'], 1)
    AddItem(ItemTable['ＨＰ２'], 1)
    AddItem(ItemTable['攻击１'], 1)
    AddItem(ItemTable['回复药'], 50)
    ChrSetStatus(ChrTable['尤莉亚上尉'], 0x00, 85)
    ChrSetStatus(ChrTable['尤莉亚上尉'], 0xFE, 0)
    EquipCmd(ChrTable['尤莉亚上尉'], ItemTable['天琴'], 0xFF)
    EquipCmd(ChrTable['尤莉亚上尉'], ItemTable['反射大衣Ⅱ'], 0xFF)
    EquipCmd(ChrTable['尤莉亚上尉'], ItemTable['合成防护靴Ⅱ'], 0xFF)
    AddCraft(ChrTable['尤莉亚上尉'], 0x0000)
    OP_BB(0x0E, 0x06, 0x0000011A)
    OP_37(0x0E, 0x80, 0x03)
    OP_37(0x0E, 0x81, 0x03)
    OP_37(0x0E, 0x82, 0x02)
    OP_37(0x0E, 0x83, 0x03)
    OP_37(0x0E, 0x84, 0x02)
    OP_37(0x0E, 0x85, 0x02)
    OP_37(0x0E, 0x86, 0x02)
    EquipCmd(ChrTable['尤莉亚上尉'], ItemTable['范围'], 0x00)
    EquipCmd(ChrTable['尤莉亚上尉'], ItemTable['行动力３'], 0x01)
    EquipCmd(ChrTable['尤莉亚上尉'], ItemTable['省ＥＰ４'], 0x03)
    EquipCmd(ChrTable['尤莉亚上尉'], ItemTable['ＨＰ４'], 0x04)
    EquipCmd(ChrTable['尤莉亚上尉'], ItemTable['防御４'], 0x05)
    EquipCmd(ChrTable['尤莉亚上尉'], ItemTable['回避４'], 0x06)
    ChrSetStatus(ChrTable['穆拉'], 0x00, 86)
    ChrSetStatus(ChrTable['穆拉'], 0xFE, 0)
    EquipCmd(ChrTable['穆拉'], ItemTable['耀晶破坏者'], 0xFF)
    EquipCmd(ChrTable['穆拉'], ItemTable['反射大衣Ⅱ'], 0xFF)
    EquipCmd(ChrTable['穆拉'], ItemTable['合成防护靴Ⅱ'], 0xFF)
    AddCraft(ChrTable['穆拉'], 0x0000)
    OP_BB(0x0F, 0x06, 0x00000114)
    OP_37(0x0F, 0x80, 0x02)
    OP_37(0x0F, 0x81, 0x03)
    OP_37(0x0F, 0x82, 0x02)
    OP_37(0x0F, 0x83, 0x02)
    OP_37(0x0F, 0x84, 0x02)
    OP_37(0x0F, 0x85, 0x03)
    OP_37(0x0F, 0x86, 0x03)
    EquipCmd(ChrTable['穆拉'], ItemTable['ＨＰ４'], 0x00)
    EquipCmd(ChrTable['穆拉'], ItemTable['行动力３'], 0x01)
    EquipCmd(ChrTable['穆拉'], ItemTable['攻击４'], 0x02)
    EquipCmd(ChrTable['穆拉'], ItemTable['阴阳'], 0x03)
    EquipCmd(ChrTable['穆拉'], ItemTable['移动３'], 0x04)
    EquipCmd(ChrTable['穆拉'], ItemTable['防御４'], 0x05)
    ChrSetStatus(ChrTable['理查德'], 0x00, 85)
    ChrSetStatus(ChrTable['理查德'], 0xFE, 0)
    AddCraft(ChrTable['理查德'], 0x0000)
    ChrSetStatus(ChrTable['凯诺娜'], 0x00, 85)
    ChrSetStatus(ChrTable['凯诺娜'], 0xFE, 0)
    AddCraft(ChrTable['凯诺娜'], 0x0000)
    MapSetFlags(0x01000000)
    FormationReset()
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0x00)
    FormationAddMember(ChrTable['约修亚'], 0xF7, 0x01)
    FormationAddMember(ChrTable['金'], 0xF8, 0x02)
    FormationAddMember(ChrTable['阿加特'], 0xF9, 0x03)
    AddItem(ItemTable['还魂胶囊'], 99)
    AddItem(ItemTable['还魂粉'], 99)
    OP_BB(0x00, 0x01, 0x00000000)
    OP_BB(0x01, 0x01, 0x00000001)
    ChrSetStatus(ChrTable['艾丝蒂尔'], 0x00, 99)
    ChrSetStatus(ChrTable['艾丝蒂尔'], 0x05, 200)
    EquipCmd(ChrTable['艾丝蒂尔'], ItemTable['黑耀珠'], 0x00)
    EquipCmd(ChrTable['艾丝蒂尔'], ItemTable['黑耀珠'], 0x01)
    EquipCmd(ChrTable['艾丝蒂尔'], ItemTable['黑耀珠'], 0x02)
    EquipCmd(ChrTable['艾丝蒂尔'], ItemTable['移动３'], 0x03)
    EquipCmd(ChrTable['艾丝蒂尔'], ItemTable['红耀珠'], 0x04)
    EquipCmd(ChrTable['艾丝蒂尔'], ItemTable['红耀珠'], 0x05)
    EquipCmd(ChrTable['艾丝蒂尔'], ItemTable['红耀珠'], 0x06)
    EquipCmd(ChrTable['艾丝蒂尔'], ItemTable['能量宝珠'], 0x03)
    EquipCmd(ChrTable['艾丝蒂尔'], ItemTable['斗魂腰带'], 0x04)
    EquipCmd(ChrTable['艾丝蒂尔'], ItemTable['大地女神之服'], 0xFF)
    EquipCmd(ChrTable['艾丝蒂尔'], ItemTable['普罗米修斯神靴'], 0xFF)
    ChrSetStatus(ChrTable['约修亚'], 0x00, 99)
    ChrSetStatus(ChrTable['约修亚'], 0x05, 200)
    EquipCmd(ChrTable['约修亚'], ItemTable['黑耀珠'], 0x00)
    EquipCmd(ChrTable['约修亚'], ItemTable['黑耀珠'], 0x01)
    EquipCmd(ChrTable['约修亚'], ItemTable['黑耀珠'], 0x02)
    EquipCmd(ChrTable['约修亚'], ItemTable['移动３'], 0x03)
    EquipCmd(ChrTable['约修亚'], ItemTable['红耀珠'], 0x04)
    EquipCmd(ChrTable['约修亚'], ItemTable['红耀珠'], 0x05)
    EquipCmd(ChrTable['约修亚'], ItemTable['红耀珠'], 0x06)
    EquipCmd(ChrTable['约修亚'], ItemTable['能量宝珠'], 0x03)
    EquipCmd(ChrTable['约修亚'], ItemTable['斗魂腰带'], 0x04)
    EquipCmd(ChrTable['约修亚'], ItemTable['大地女神之服'], 0xFF)
    EquipCmd(ChrTable['约修亚'], ItemTable['普罗米修斯神靴'], 0xFF)
    ChrSetStatus(ChrTable['雪拉扎德'], 0x00, 99)
    ChrSetStatus(ChrTable['雪拉扎德'], 0x05, 200)
    EquipCmd(ChrTable['雪拉扎德'], ItemTable['黑耀珠'], 0x00)
    EquipCmd(ChrTable['雪拉扎德'], ItemTable['黑耀珠'], 0x01)
    EquipCmd(ChrTable['雪拉扎德'], ItemTable['黑耀珠'], 0x02)
    EquipCmd(ChrTable['雪拉扎德'], ItemTable['移动３'], 0x03)
    EquipCmd(ChrTable['雪拉扎德'], ItemTable['红耀珠'], 0x04)
    EquipCmd(ChrTable['雪拉扎德'], ItemTable['红耀珠'], 0x05)
    EquipCmd(ChrTable['雪拉扎德'], ItemTable['红耀珠'], 0x06)
    EquipCmd(ChrTable['雪拉扎德'], ItemTable['能量宝珠'], 0x03)
    EquipCmd(ChrTable['雪拉扎德'], ItemTable['斗魂腰带'], 0x04)
    EquipCmd(ChrTable['雪拉扎德'], ItemTable['大地女神之服'], 0xFF)
    EquipCmd(ChrTable['雪拉扎德'], ItemTable['普罗米修斯神靴'], 0xFF)
    ChrSetStatus(ChrTable['奥利维尔'], 0x00, 99)
    ChrSetStatus(ChrTable['奥利维尔'], 0x05, 200)
    EquipCmd(ChrTable['奥利维尔'], ItemTable['黑耀珠'], 0x00)
    EquipCmd(ChrTable['奥利维尔'], ItemTable['黑耀珠'], 0x01)
    EquipCmd(ChrTable['奥利维尔'], ItemTable['黑耀珠'], 0x02)
    EquipCmd(ChrTable['奥利维尔'], ItemTable['移动３'], 0x03)
    EquipCmd(ChrTable['奥利维尔'], ItemTable['红耀珠'], 0x04)
    EquipCmd(ChrTable['奥利维尔'], ItemTable['红耀珠'], 0x05)
    EquipCmd(ChrTable['奥利维尔'], ItemTable['红耀珠'], 0x06)
    EquipCmd(ChrTable['奥利维尔'], ItemTable['能量宝珠'], 0x03)
    EquipCmd(ChrTable['奥利维尔'], ItemTable['斗魂腰带'], 0x04)
    EquipCmd(ChrTable['奥利维尔'], ItemTable['大地女神之服'], 0xFF)
    EquipCmd(ChrTable['奥利维尔'], ItemTable['普罗米修斯神靴'], 0xFF)
    ChrSetStatus(ChrTable['科洛丝'], 0x00, 99)
    ChrSetStatus(ChrTable['科洛丝'], 0x05, 200)
    EquipCmd(ChrTable['科洛丝'], ItemTable['黑耀珠'], 0x00)
    EquipCmd(ChrTable['科洛丝'], ItemTable['黑耀珠'], 0x01)
    EquipCmd(ChrTable['科洛丝'], ItemTable['黑耀珠'], 0x02)
    EquipCmd(ChrTable['科洛丝'], ItemTable['移动３'], 0x03)
    EquipCmd(ChrTable['科洛丝'], ItemTable['红耀珠'], 0x04)
    EquipCmd(ChrTable['科洛丝'], ItemTable['红耀珠'], 0x05)
    EquipCmd(ChrTable['科洛丝'], ItemTable['红耀珠'], 0x06)
    EquipCmd(ChrTable['科洛丝'], ItemTable['能量宝珠'], 0x03)
    EquipCmd(ChrTable['科洛丝'], ItemTable['斗魂腰带'], 0x04)
    EquipCmd(ChrTable['科洛丝'], ItemTable['大地女神之服'], 0xFF)
    EquipCmd(ChrTable['科洛丝'], ItemTable['普罗米修斯神靴'], 0xFF)
    ChrSetStatus(ChrTable['阿加特'], 0x00, 99)
    ChrSetStatus(ChrTable['阿加特'], 0x05, 200)
    EquipCmd(ChrTable['阿加特'], ItemTable['黑耀珠'], 0x00)
    EquipCmd(ChrTable['阿加特'], ItemTable['黑耀珠'], 0x01)
    EquipCmd(ChrTable['阿加特'], ItemTable['黑耀珠'], 0x02)
    EquipCmd(ChrTable['阿加特'], ItemTable['移动３'], 0x03)
    EquipCmd(ChrTable['阿加特'], ItemTable['红耀珠'], 0x04)
    EquipCmd(ChrTable['阿加特'], ItemTable['红耀珠'], 0x05)
    EquipCmd(ChrTable['阿加特'], ItemTable['红耀珠'], 0x06)
    EquipCmd(ChrTable['阿加特'], ItemTable['能量宝珠'], 0x03)
    EquipCmd(ChrTable['阿加特'], ItemTable['斗魂腰带'], 0x04)
    EquipCmd(ChrTable['阿加特'], ItemTable['大地女神之服'], 0xFF)
    EquipCmd(ChrTable['阿加特'], ItemTable['普罗米修斯神靴'], 0xFF)
    ChrSetStatus(ChrTable['提妲'], 0x00, 99)
    ChrSetStatus(ChrTable['提妲'], 0x05, 200)
    EquipCmd(ChrTable['提妲'], ItemTable['黑耀珠'], 0x00)
    EquipCmd(ChrTable['提妲'], ItemTable['黑耀珠'], 0x01)
    EquipCmd(ChrTable['提妲'], ItemTable['黑耀珠'], 0x02)
    EquipCmd(ChrTable['提妲'], ItemTable['移动３'], 0x03)
    EquipCmd(ChrTable['提妲'], ItemTable['红耀珠'], 0x04)
    EquipCmd(ChrTable['提妲'], ItemTable['红耀珠'], 0x05)
    EquipCmd(ChrTable['提妲'], ItemTable['红耀珠'], 0x06)
    EquipCmd(ChrTable['提妲'], ItemTable['能量宝珠'], 0x03)
    EquipCmd(ChrTable['提妲'], ItemTable['斗魂腰带'], 0x04)
    EquipCmd(ChrTable['提妲'], ItemTable['大地女神之服'], 0xFF)
    EquipCmd(ChrTable['提妲'], ItemTable['普罗米修斯神靴'], 0xFF)
    ChrSetStatus(ChrTable['金'], 0x00, 99)
    ChrSetStatus(ChrTable['金'], 0x05, 200)
    EquipCmd(ChrTable['金'], ItemTable['黑耀珠'], 0x00)
    EquipCmd(ChrTable['金'], ItemTable['黑耀珠'], 0x01)
    EquipCmd(ChrTable['金'], ItemTable['黑耀珠'], 0x02)
    EquipCmd(ChrTable['金'], ItemTable['移动３'], 0x03)
    EquipCmd(ChrTable['金'], ItemTable['红耀珠'], 0x04)
    EquipCmd(ChrTable['金'], ItemTable['红耀珠'], 0x05)
    EquipCmd(ChrTable['金'], ItemTable['红耀珠'], 0x06)
    EquipCmd(ChrTable['金'], ItemTable['能量宝珠'], 0x03)
    EquipCmd(ChrTable['金'], ItemTable['斗魂腰带'], 0x04)
    EquipCmd(ChrTable['金'], ItemTable['大地女神之服'], 0xFF)
    EquipCmd(ChrTable['金'], ItemTable['普罗米修斯神靴'], 0xFF)
    ChrSetStatus(ChrTable['凯文神父'], 0x00, 99)
    ChrSetStatus(ChrTable['凯文神父'], 0x05, 200)
    EquipCmd(ChrTable['凯文神父'], ItemTable['黑耀珠'], 0x00)
    EquipCmd(ChrTable['凯文神父'], ItemTable['黑耀珠'], 0x01)
    EquipCmd(ChrTable['凯文神父'], ItemTable['黑耀珠'], 0x02)
    EquipCmd(ChrTable['凯文神父'], ItemTable['移动３'], 0x03)
    EquipCmd(ChrTable['凯文神父'], ItemTable['红耀珠'], 0x04)
    EquipCmd(ChrTable['凯文神父'], ItemTable['红耀珠'], 0x05)
    EquipCmd(ChrTable['凯文神父'], ItemTable['红耀珠'], 0x06)
    EquipCmd(ChrTable['凯文神父'], ItemTable['能量宝珠'], 0x03)
    EquipCmd(ChrTable['凯文神父'], ItemTable['斗魂腰带'], 0x04)
    EquipCmd(ChrTable['凯文神父'], ItemTable['大地女神之服'], 0xFF)
    EquipCmd(ChrTable['凯文神父'], ItemTable['普罗米修斯神靴'], 0xFF)
    ChrSetStatus(ChrTable['亚妮拉丝'], 0x00, 99)
    ChrSetStatus(ChrTable['亚妮拉丝'], 0x05, 200)
    EquipCmd(ChrTable['亚妮拉丝'], ItemTable['黑耀珠'], 0x00)
    EquipCmd(ChrTable['亚妮拉丝'], ItemTable['黑耀珠'], 0x01)
    EquipCmd(ChrTable['亚妮拉丝'], ItemTable['黑耀珠'], 0x02)
    EquipCmd(ChrTable['亚妮拉丝'], ItemTable['移动３'], 0x03)
    EquipCmd(ChrTable['亚妮拉丝'], ItemTable['红耀珠'], 0x04)
    EquipCmd(ChrTable['亚妮拉丝'], ItemTable['红耀珠'], 0x05)
    EquipCmd(ChrTable['亚妮拉丝'], ItemTable['红耀珠'], 0x06)
    EquipCmd(ChrTable['亚妮拉丝'], ItemTable['能量宝珠'], 0x03)
    EquipCmd(ChrTable['亚妮拉丝'], ItemTable['斗魂腰带'], 0x04)
    EquipCmd(ChrTable['亚妮拉丝'], ItemTable['大地女神之服'], 0xFF)
    EquipCmd(ChrTable['亚妮拉丝'], ItemTable['普罗米修斯神靴'], 0xFF)
    ChrSetStatus(ChrTable['乔丝特'], 0x00, 99)
    ChrSetStatus(ChrTable['乔丝特'], 0x05, 200)
    EquipCmd(ChrTable['乔丝特'], ItemTable['黑耀珠'], 0x00)
    EquipCmd(ChrTable['乔丝特'], ItemTable['黑耀珠'], 0x01)
    EquipCmd(ChrTable['乔丝特'], ItemTable['黑耀珠'], 0x02)
    EquipCmd(ChrTable['乔丝特'], ItemTable['移动３'], 0x03)
    EquipCmd(ChrTable['乔丝特'], ItemTable['红耀珠'], 0x04)
    EquipCmd(ChrTable['乔丝特'], ItemTable['红耀珠'], 0x05)
    EquipCmd(ChrTable['乔丝特'], ItemTable['红耀珠'], 0x06)
    EquipCmd(ChrTable['乔丝特'], ItemTable['能量宝珠'], 0x03)
    EquipCmd(ChrTable['乔丝特'], ItemTable['斗魂腰带'], 0x04)
    EquipCmd(ChrTable['乔丝特'], ItemTable['大地女神之服'], 0xFF)
    EquipCmd(ChrTable['乔丝特'], ItemTable['普罗米修斯神靴'], 0xFF)
    ChrSetStatus(ChrTable['理查德'], 0x00, 99)
    ChrSetStatus(ChrTable['理查德'], 0x05, 200)
    EquipCmd(ChrTable['理查德'], ItemTable['黑耀珠'], 0x00)
    EquipCmd(ChrTable['理查德'], ItemTable['黑耀珠'], 0x01)
    EquipCmd(ChrTable['理查德'], ItemTable['黑耀珠'], 0x02)
    EquipCmd(ChrTable['理查德'], ItemTable['移动３'], 0x03)
    EquipCmd(ChrTable['理查德'], ItemTable['红耀珠'], 0x04)
    EquipCmd(ChrTable['理查德'], ItemTable['红耀珠'], 0x05)
    EquipCmd(ChrTable['理查德'], ItemTable['红耀珠'], 0x06)
    EquipCmd(ChrTable['理查德'], ItemTable['能量宝珠'], 0x03)
    EquipCmd(ChrTable['理查德'], ItemTable['斗魂腰带'], 0x04)
    EquipCmd(ChrTable['理查德'], ItemTable['大地女神之服'], 0xFF)
    EquipCmd(ChrTable['理查德'], ItemTable['普罗米修斯神靴'], 0xFF)
    ChrSetStatus(ChrTable['凯诺娜'], 0x00, 99)
    ChrSetStatus(ChrTable['凯诺娜'], 0x05, 200)
    EquipCmd(ChrTable['凯诺娜'], ItemTable['黑耀珠'], 0x00)
    EquipCmd(ChrTable['凯诺娜'], ItemTable['黑耀珠'], 0x01)
    EquipCmd(ChrTable['凯诺娜'], ItemTable['黑耀珠'], 0x02)
    EquipCmd(ChrTable['凯诺娜'], ItemTable['移动３'], 0x03)
    EquipCmd(ChrTable['凯诺娜'], ItemTable['红耀珠'], 0x04)
    EquipCmd(ChrTable['凯诺娜'], ItemTable['红耀珠'], 0x05)
    EquipCmd(ChrTable['凯诺娜'], ItemTable['红耀珠'], 0x06)
    EquipCmd(ChrTable['凯诺娜'], ItemTable['能量宝珠'], 0x03)
    EquipCmd(ChrTable['凯诺娜'], ItemTable['斗魂腰带'], 0x04)
    EquipCmd(ChrTable['凯诺娜'], ItemTable['大地女神之服'], 0xFF)
    EquipCmd(ChrTable['凯诺娜'], ItemTable['普罗米修斯神靴'], 0xFF)
    ChrSetStatus(ChrTable['克鲁茨'], 0x00, 99)
    ChrSetStatus(ChrTable['克鲁茨'], 0x05, 200)
    EquipCmd(ChrTable['克鲁茨'], ItemTable['黑耀珠'], 0x00)
    EquipCmd(ChrTable['克鲁茨'], ItemTable['黑耀珠'], 0x01)
    EquipCmd(ChrTable['克鲁茨'], ItemTable['黑耀珠'], 0x02)
    EquipCmd(ChrTable['克鲁茨'], ItemTable['移动３'], 0x03)
    EquipCmd(ChrTable['克鲁茨'], ItemTable['红耀珠'], 0x04)
    EquipCmd(ChrTable['克鲁茨'], ItemTable['红耀珠'], 0x05)
    EquipCmd(ChrTable['克鲁茨'], ItemTable['红耀珠'], 0x06)
    EquipCmd(ChrTable['克鲁茨'], ItemTable['能量宝珠'], 0x03)
    EquipCmd(ChrTable['克鲁茨'], ItemTable['斗魂腰带'], 0x04)
    EquipCmd(ChrTable['克鲁茨'], ItemTable['大地女神之服'], 0xFF)
    EquipCmd(ChrTable['克鲁茨'], ItemTable['普罗米修斯神靴'], 0xFF)
    ChrSetStatus(ChrTable['尤莉亚上尉'], 0x00, 99)
    ChrSetStatus(ChrTable['尤莉亚上尉'], 0x05, 200)
    EquipCmd(ChrTable['尤莉亚上尉'], ItemTable['黑耀珠'], 0x00)
    EquipCmd(ChrTable['尤莉亚上尉'], ItemTable['黑耀珠'], 0x01)
    EquipCmd(ChrTable['尤莉亚上尉'], ItemTable['黑耀珠'], 0x02)
    EquipCmd(ChrTable['尤莉亚上尉'], ItemTable['移动３'], 0x03)
    EquipCmd(ChrTable['尤莉亚上尉'], ItemTable['红耀珠'], 0x04)
    EquipCmd(ChrTable['尤莉亚上尉'], ItemTable['红耀珠'], 0x05)
    EquipCmd(ChrTable['尤莉亚上尉'], ItemTable['红耀珠'], 0x06)
    EquipCmd(ChrTable['尤莉亚上尉'], ItemTable['能量宝珠'], 0x03)
    EquipCmd(ChrTable['尤莉亚上尉'], ItemTable['斗魂腰带'], 0x04)
    EquipCmd(ChrTable['尤莉亚上尉'], ItemTable['大地女神之服'], 0xFF)
    EquipCmd(ChrTable['尤莉亚上尉'], ItemTable['普罗米修斯神靴'], 0xFF)
    ChrSetStatus(ChrTable['穆拉'], 0x00, 99)
    ChrSetStatus(ChrTable['穆拉'], 0x05, 200)
    EquipCmd(ChrTable['穆拉'], ItemTable['黑耀珠'], 0x00)
    EquipCmd(ChrTable['穆拉'], ItemTable['黑耀珠'], 0x01)
    EquipCmd(ChrTable['穆拉'], ItemTable['黑耀珠'], 0x02)
    EquipCmd(ChrTable['穆拉'], ItemTable['移动３'], 0x03)
    EquipCmd(ChrTable['穆拉'], ItemTable['红耀珠'], 0x04)
    EquipCmd(ChrTable['穆拉'], ItemTable['红耀珠'], 0x05)
    EquipCmd(ChrTable['穆拉'], ItemTable['红耀珠'], 0x06)
    EquipCmd(ChrTable['穆拉'], ItemTable['能量宝珠'], 0x03)
    EquipCmd(ChrTable['穆拉'], ItemTable['斗魂腰带'], 0x04)
    EquipCmd(ChrTable['穆拉'], ItemTable['大地女神之服'], 0xFF)
    EquipCmd(ChrTable['穆拉'], ItemTable['普罗米修斯神靴'], 0xFF)
    EquipCmd(ChrTable['艾丝蒂尔'], ItemTable['叶隐'], 0x00)
    EquipCmd(ChrTable['艾丝蒂尔'], ItemTable['麒麟具'], 0xFF)
    EquipCmd(ChrTable['约修亚'], ItemTable['凤凰剑（凤·凰）'], 0xFF)
    EquipCmd(ChrTable['雪拉扎德'], ItemTable['天狼鞭'], 0xFF)
    EquipCmd(ChrTable['奥利维尔'], ItemTable['殂击神'], 0xFF)
    EquipCmd(ChrTable['科洛丝'], ItemTable['七星剑'], 0xFF)
    EquipCmd(ChrTable['阿加特'], ItemTable['奇剑「鬼灭之刃」'], 0xFF)
    EquipCmd(ChrTable['提妲'], ItemTable['九龙炮'], 0xFF)
    EquipCmd(ChrTable['金'], ItemTable['千手观音'], 0xFF)

    def _loc_8B5(): pass

    label('loc_8B5')

    MapSetFlags(0x00000001)
    MapClearFlags(0x00000020)
    MapClearFlags(0x00400000)

    Return()

# id: 0x0002 offset: 0x8C5
@scena.Code('func_02_8C5')
def func_02_8C5():
    OP_D7(0x01, 50000, 0)

    Return()

# id: 0x0003 offset: 0x8CE
@scena.Code('func_03_8CE')
def func_03_8CE():
    Return()

# id: 0x0004 offset: 0x8CF
@scena.Code('func_04_8CF')
def func_04_8CF():
    Call(0, 0x000B)

    Return()

# id: 0x0005 offset: 0x8D4
@scena.Code('func_05_8D4')
def func_05_8D4():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 2, 0x12)),
            Expr.Return,
        ),
        'loc_8F4',
    )

    ChrTalk(
        0x00FE,
        (
            '立着地点标旗哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8F4(): pass

    label('loc_8F4')

    SetScenaFlags(ScenaFlag(0x0002, 2, 0x12))
    SetMessageWindowPos(100, 100, 15, 2)

    Talk(
        (
            '#200W可以指定坐标显示哦。',
            TxtCtl.Enter,
            '\n',
            '#W真的哦',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            '#20A2等两秒～',
            TxtCtl.Enter,
            '#A如果不指定坐标，\n',
            '画面中央是中心圆（center ring）～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    Talk(
        (
            '请指定恢复时的默认坐标。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    ChrTalk(
        0x00FE,
        (
            '#010F#1P停止左上',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#010F#2P停止右上',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#010F#3P停止左下',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#010F#4P停止右下',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#010F#5P停止直上',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#010F#6P停止直下',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只要按下F11，就能看见\n',
            '任务区域等地，明白了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#010F我要，和爱娜！白头偕老！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0001,
        (
            '#020F哦哦？哈～哈、哈、哈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0001,
        (
            '#020F没想到会在这种地方\n',
            '遇见爱娜小姐的心上人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkSetChrName('约修亚')

    Talk(
        (
            '#000F暑假已经结束了。',
            TxtCtl.Enter,
            '\n',
            '#4S啊啊啊啊啊',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_61(0x0101)

    Talk(
        (
            '#F#2Sあいうえお#10R a   i   u   e   o#',
            TxtCtl.Enter,
            '\n',
            'かきくけこ#10R ka  ki  ku  ke  ko#さしすせそ#10R sa  si  su  se  so#\n',
            '真是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0xB81
@scena.Code('func_06_B81')
def func_06_B81():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_BA5',
    )

    OP_8D(0x00FE, 5000, -5000, 15000, 9000, 2000)
    Yield()

    Jump('func_06_B81')

    def _loc_BA5(): pass

    label('loc_BA5')

    Return()

# id: 0x0007 offset: 0xBA6
@scena.Code('func_07_BA6')
def func_07_BA6():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_BE1',
    )

    OP_70(0x0001, 50)
    OP_8D(0x00FE, -10000, -10000, 1000, 1000, 2000)
    OP_6F(0x0001, 0)
    OP_72(0x0001, 0x0008)
    Sleep(2000)

    Jump('func_07_BA6')

    def _loc_BE1(): pass

    label('loc_BE1')

    Return()

# id: 0x0008 offset: 0xBE2
@scena.Code('func_08_BE2')
def func_08_BE2():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_BF6',
    )

    ChrSetDirection(0x00FE, 180, 5000)
    Yield()

    Jump('func_08_BE2')

    def _loc_BF6(): pass

    label('loc_BF6')

    Return()

# id: 0x0009 offset: 0xBF7
@scena.Code('func_09_BF7')
def func_09_BF7():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_C1A',
    )

    OP_8D(0x0000, 10000, 10000, -10000, -10000, 2000)

    Jump('func_09_BF7')

    def _loc_C1A(): pass

    label('loc_C1A')

    Return()

# id: 0x000A offset: 0xC1B
@scena.Code('func_0A_C1B')
def func_0A_C1B():
    OP_A1(0x000A, 0x0004)
    ChrSetFlags(0x000A, 0x0004)
    ChrClearFlags(0x000A, 0x0100)
    ChrSetPos(0x000A, 0, 0, 0, 0)
    OP_98(0x00, 0x000A)
    OP_98(0x01, 10000, 2000, 10000)
    OP_98(0x01, 5000, 6000, 20000)

    @scena.Lambda('lambda_0C61')
    def lambda_0C61():
        OP_98(0x02, 0x000A, 2000, 0x06)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0C61)

    WaitForThreadExit(0x000A, 0x0002)
    ChrWalkTo(0x000A, -3000, 0, 0, 2000, 0x00)
    OP_98(0x00, 0x000A)
    OP_98(0x01, 7000, 0, 5000)
    OP_98(0x01, 10000, 2000, 8000)
    OP_98(0x01, 15000, 5000, 7000)
    OP_98(0x02, 0x000A, 2000, 0x02)
    OP_98(0x00, 0x000A)
    OP_98(0x01, 10000, -5000, 2000)
    OP_98(0x01, 10000, 10000, -5000)
    OP_98(0x02, 0x000A, 2000, 0x02)

    Return()

# id: 0x000B offset: 0xCE5
@scena.Code('func_0B_CE5')
def func_0B_CE5():
    OP_16(0x01)
    EventBegin(0x00)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Talk(
        (
            '取得号',
            TxtCtl.Enter,
        ),
    )

    OP_57(0x0000, 0x0000, 0x0012, '#1C菜单标题')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_D18(): pass

    label('loc_D18')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_165D',
    )

    Menu(
        0,
        -1,
        -1,
        1,
        (
            TXT(0x00, '测试地图\n'),
            TXT(0x01, '游戏地图\n'),
            TXT(0x02, '角色一览\n'),
            TXT(0x03, '魔兽一览\n'),
            TXT(0x04, '战斗\n'),
            TXT(0x05, '战斗（魔兽算法测试）\n'),
            TXT(0x06, '战斗（地图确认）\n'),
            TXT(0x07, '迷你游戏\n'),
            TXT(0x08, '事件列表\n'),
            TXT(0x09, '商店测试\n'),
            TXT(0x0A, '前篇后编角色替换新画\n'),
            TXT(0x0B, '*Trap Land\n'),
            TXT(0x0C, '头像\n'),
            TXT(0x0D, '组队选择菜单\n'),
            TXT(0x0E, '*模糊（blur）\n'),
            TXT(0x0F, '道具菜单\n'),
            TXT(0x10, '*出不来！存档菜单\n'),
            TXT(0x11, '手册标志树立完毕\n'),
            TXT(0x12, '菜谱收集完整\n'),
            TXT(0x13, '游戏通关\n'),
            TXT(0x14, 'Camp菜单\n'),
            TXT(0x15, '动画播放·停止\n'),
            TXT(0x16, '队伍变更\n'),
            TXT(0x17, 'Disk Change\n'),
            TXT(0x18, '检查继承标志\n'),
            TXT(0x19, '检查２周目标志（カジノ）\n'),
            TXT(0x1A, '取消\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_16(0x01)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_EE8'),
        (0x00000001, 'loc_EFB'),
        (0x00000002, 'loc_F02'),
        (0x00000003, 'loc_F09'),
        (0x00000004, 'loc_F10'),
        (0x00000005, 'loc_F17'),
        (0x00000006, 'loc_F1E'),
        (0x00000007, 'loc_F25'),
        (0x00000008, 'loc_F2C'),
        (0x00000009, 'loc_F36'),
        (0x0000000A, 'loc_F42'),
        (0x0000000B, 'loc_FF0'),
        (0x0000000C, 'loc_FFC'),
        (0x0000000D, 'loc_11FB'),
        (0x0000000E, 'loc_1299'),
        (0x0000000F, 'loc_12D4'),
        (0x00000010, 'loc_12DB'),
        (0x00000011, 'loc_12DF'),
        (0x00000012, 'loc_12E6'),
        (0x00000013, 'loc_12ED'),
        (0x00000014, 'loc_1309'),
        (0x00000015, 'loc_155C'),
        (0x00000016, 'loc_1589'),
        (0x00000017, 'loc_159D'),
        (0x00000018, 'loc_163F'),
        (0x00000019, 'loc_1646'),
        (-1, 'loc_164D'),
    )

    def _loc_EE8(): pass

    label('loc_EE8')

    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C5313._SN', 100, 0, 0)
    IdleLoop()
    Call(0, 0x000F)

    Jump('loc_165A')

    def _loc_EFB(): pass

    label('loc_EFB')

    Call(3, 0x0006)

    Jump('loc_165A')

    def _loc_F02(): pass

    label('loc_F02')

    Call(3, 0x0000)

    Jump('loc_165A')

    def _loc_F09(): pass

    label('loc_F09')

    Call(3, 0x0003)

    Jump('loc_165A')

    def _loc_F10(): pass

    label('loc_F10')

    Call(2, 0x0000)

    Jump('loc_165A')

    def _loc_F17(): pass

    label('loc_F17')

    Call(1, 0x0000)

    Jump('loc_165A')

    def _loc_F1E(): pass

    label('loc_F1E')

    Call(2, 0x0001)

    Jump('loc_165A')

    def _loc_F25(): pass

    label('loc_F25')

    Call(2, 0x003B)

    Jump('loc_165A')

    def _loc_F2C(): pass

    label('loc_F2C')

    OP_66(0x0001)
    Call(4, 0x0000)

    Jump('loc_165A')

    def _loc_F36(): pass

    label('loc_F36')

    OP_5F(0x0000)
    OP_56(0x00)
    Call(0, 0x0015)

    Jump('loc_165A')

    def _loc_F42(): pass

    label('loc_F42')

    Menu(
        1,
        -1,
        -1,
        1,
        (
            TXT(0x00, '艾丝蒂尔后篇，约修亚后篇\n'),
            TXT(0x01, '艾丝蒂尔前篇，约修亚前篇\n'),
            TXT(0x02, '约修亚后半，科洛丝后半\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_FAC'),
        (0x00000001, 'loc_FBD'),
        (0x00000002, 'loc_FCE'),
        (-1, 'loc_FDF'),
    )

    def _loc_FAC(): pass

    label('loc_FAC')

    OP_BB(0x00, 0x01, 0x00000000)
    OP_BB(0x01, 0x01, 0x00000001)

    Jump('loc_FDF')

    def _loc_FBD(): pass

    label('loc_FBD')

    OP_BB(0x00, 0x01, 0x0000001E)
    OP_BB(0x01, 0x01, 0x0000001F)

    Jump('loc_FDF')

    def _loc_FCE(): pass

    label('loc_FCE')

    OP_BB(0x04, 0x01, 0x0000001D)
    OP_BB(0x01, 0x01, 0x0000001C)

    Jump('loc_FDF')

    def _loc_FDF(): pass

    label('loc_FDF')

    OP_5F(0x0001)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_BD()

    Jump('loc_165A')

    def _loc_FF0(): pass

    label('loc_FF0')

    NewScene('ED6_DT21/A0019._SN', 0, 0, 0)
    IdleLoop()

    Jump('loc_165A')

    def _loc_FFC(): pass

    label('loc_FFC')

    OP_5F(0x0000)
    OP_56(0x00)
    Sleep(1000)

    OP_D9(0x00, 'CTI00110')
    Sleep(2000)

    OP_D9(0x01)
    OP_C5(0x00, 0, 0, 512, 512, 0, 0, 768, 512, 0, 0, 511, 511, 0x00FFFFFF, 0x00, 'C_VIS000._CH')
    OP_C6(0x00, 0x03, -1, 1000, 0)
    Sleep(2000)

    OP_C5(0x01, -100, -100, 100, 100, 340, 250, 768, 512, 0, 0, 255, 255, 0x00FFFFFF, 0x00, 'C_VIS001._CH')
    OP_C6(0x01, 0x03, -1, 1000, 0)
    Sleep(2000)

    OP_C5(0x00, -100, -100, 100, 100, 360, 260, 768, 512, 0, 0, 255, 255, 0x00FFFFFF, 0x00, 'C_VIS002._CH')
    OP_C6(0x00, 0x03, -1, 1000, 0)
    Sleep(2000)

    OP_C5(0x02, -100, -100, 100, 100, 380, 260, 768, 512, 0, 0, 255, 255, 0x00FFFFFF, 0x00, 'C_VIS002._CH')
    OP_C6(0x02, 0x03, -1, 1000, 0)
    Sleep(2000)

    OP_C5(0x03, -100, -100, 100, 100, 400, 260, 768, 512, 0, 0, 255, 255, 0x00FFFFFF, 0x00, 'C_VIS002._CH')
    OP_C6(0x03, 0x03, -1, 1000, 0)
    OP_C6(0x00, 0x00, 0, 0, 1000)
    OP_C6(0x00, 0x02, 90000, 2000, 0)
    OP_C7(0x00, 0x00, 0x00)

    Talk(
        (
            '噢',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_C6(0x00, 0x00, 360000, 260000, 0)
    Sleep(1000)

    OP_C6(0x01, 0x04, 0, 0, 0)
    Sleep(1000)

    OP_C6(0x00, 0x03, 16777215, 1000, 0)
    OP_C6(0x00, 0x01, 0, 1000, 1000)
    OP_C6(0x01, 0x03, 16777215, 1000, 0)
    OP_C6(0x02, 0x03, 16777215, 500, 0)
    OP_C6(0x03, 0x01, 10000, 0, 500)
    OP_C7(0x00, 0xFF, 0x03)
    OP_C7(0x01, 0xFF, 0x00)

    Jump('loc_165A')

    def _loc_11FB(): pass

    label('loc_11FB')

    OP_5F(0x0000)
    OP_56(0x00)

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            0x00FF,
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['约修亚'],
            ChrTable['雪拉扎德'],
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            ChrTable['阿加特'],
            ChrTable['提妲'],
            ChrTable['金'],
            ChrTable['凯文神父'],
            ChrTable['亚妮拉丝'],
            ChrTable['克鲁茨'],
            ChrTable['乔丝特'],
            ChrTable['穆拉'],
            ChrTable['尤莉亚上尉'],
            ChrTable['理查德'],
            ChrTable['凯诺娜'],
            0xFFFF,
        ),
    )

    ChrTalk(
        0x00F8,
        (
            'Ｏｋ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_CB(0xF7)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1256',
    )

    ChrTalk(
        0x00F7,
        (
            '队友１科洛丝',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_1295')

    def _loc_1256(): pass

    label('loc_1256')

    If(
        (
            (Expr.Eval, "OP_CB(0xF7)"),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1277',
    )

    ChrTalk(
        0x00F7,
        (
            '队友１约修亚',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_1295')

    def _loc_1277(): pass

    label('loc_1277')

    If(
        (
            (Expr.Eval, "OP_CB(0xF7)"),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1295',
    )

    ChrTalk(
        0x00F7,
        (
            '队友１阿加特',
            TxtCtl.Enter,
        ),
    )

    def _loc_1295(): pass

    label('loc_1295')

    CloseMessageWindow()

    Jump('loc_165A')

    def _loc_1299(): pass

    label('loc_1299')

    Blur(1000, 0xBBFFFFFF, 0, 0x00, 0)

    ChrTalk(
        0x00F6,
        (
            '*模糊（blur）',
            TxtCtl.Enter,
        ),
    )

    Sleep(2000)

    OP_15(0x000001F4)

    ChrTalk(
        0x00F6,
        (
            '那么',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_165A')

    def _loc_12D4(): pass

    label('loc_12D4')

    OP_18(0x00, 0x00, 0x00)

    Jump('loc_165A')

    def _loc_12DB(): pass

    label('loc_12DB')

    ShowSaveMenu()

    Jump('loc_165A')

    def _loc_12DF(): pass

    label('loc_12DF')

    Call(5, 0x0000)

    Jump('loc_165A')

    def _loc_12E6(): pass

    label('loc_12E6')

    Call(5, 0x0001)

    Jump('loc_165A')

    def _loc_12ED(): pass

    label('loc_12ED')

    ExecExpressionWithVar(
        0x31,
        (
            (Expr.PushLong, 0x12B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetScenaFlags(ScenaFlag(0x0455, 6, 0x22AE))
    FadeOut(500, 0, -1)
    ShowSaveMenu()
    OP_B4(0x01)

    Jump('loc_165A')

    def _loc_1309(): pass

    label('loc_1309')

    EventBegin(0x00)
    OP_5F(0x0000)
    OP_56(0x00)
    ClearScenaFlags(ScenaFlag(0x0002, 6, 0x16))
    def _loc_1313(): pass

    label('loc_1313')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1546',
    )

    FadeOut(1000, 0, -1)
    OP_0D()

    Talk(
        (
            TxtCtl.ShowAll,
            0x18,
            (TxtCtl.SetColor, 0x5),
            '※进行队伍的重新编组。\n',
            '　更换队员，进行必要的装备变更，\n',
            '　确定后，请选择【继续】。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, '【编成队伍】\n'),
            TXT(0x01, '【变更装备】\n'),
            TXT(0x02, '【继续】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)
    OP_56(0x00)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_143E',
    )

    SetScenaFlags(ScenaFlag(0x0002, 6, 0x16))
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※进行队伍的重新编组。\n',
            '　请选择２名固定成员以外的同行者。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Sleep(100)

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['凯文神父'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['雪拉扎德'],
            ChrTable['提妲'],
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            ChrTable['金'],
            0xFFFF,
        ),
    )

    Jump('loc_1543')

    def _loc_143E(): pass

    label('loc_143E')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_14A9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 6, 0x16)),
            Expr.Return,
        ),
        'loc_1477',
    )

    OP_C0(0x13, 0x00000078, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)

    Jump('loc_14A6')

    def _loc_1477(): pass

    label('loc_1477')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※请在进行队伍的编组之后再选择。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Sleep(100)

    def _loc_14A6(): pass

    label('loc_14A6')

    Jump('loc_1543')

    def _loc_14A9(): pass

    label('loc_14A9')

    TalkSetChrName('')

    Talk(
        (
            TxtCtl.ShowAll,
            0x18,
            (TxtCtl.SetColor, 0x5),
            '可以继续事件剧情了吗？',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, '【是】\n'),
            TXT(0x01, '【否】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)
    OP_56(0x00)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1527',
    )

    TalkSetChrName('')

    Talk(
        (
            TxtCtl.ShowAll,
            0x18,
            (TxtCtl.SetColor, 0x5),
            '继续事件发展。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_1546')

    def _loc_1527(): pass

    label('loc_1527')

    TalkSetChrName('')

    Talk(
        (
            TxtCtl.ShowAll,
            0x18,
            (TxtCtl.SetColor, 0x5),
            '返回选择画面。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_1543(): pass

    label('loc_1543')

    Jump('loc_1313')

    def _loc_1546(): pass

    label('loc_1546')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeIn(0, 0)
    OP_0D()

    Jump('loc_165A')

    def _loc_155C(): pass

    label('loc_155C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 5, 0x15)),
            Expr.Return,
        ),
        'loc_1570',
    )

    PlayMovie(0x01, '', 0x0000, 0x0000)
    ClearScenaFlags(ScenaFlag(0x0002, 5, 0x15))

    Jump('loc_1586')

    def _loc_1570(): pass

    label('loc_1570')

    PlayMovie(0x00, 'ED6_DT41.dat', 0x0000, 0x0000)
    SetScenaFlags(ScenaFlag(0x0002, 5, 0x15))

    def _loc_1586(): pass

    label('loc_1586')

    Jump('loc_165A')

    def _loc_1589(): pass

    label('loc_1589')

    Call(0, 0x001B)
    FadeIn(0, 0)
    Call(0, 0x001C)

    Jump('loc_165A')

    def _loc_159D(): pass

    label('loc_159D')

    OP_5F(0x0000)

    Talk(
        (
            'RAM Saving!',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_E9(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xCA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_15CF',
    )

    Talk(
        (
            'RAM Load！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_15CF(): pass

    label('loc_15CF')

    Talk(
        (
            'Disk chaaaaange!',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    If(
        (
            (Expr.PushValueByIndex, 0xC8),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_15F6',
    )

    OP_E6(0x02)

    Jump('loc_15F8')

    def _loc_15F6(): pass

    label('loc_15F6')

    OP_E6(0x01)

    def _loc_15F8(): pass

    label('loc_15F8')

    If(
        (
            (Expr.PushValueByIndex, 0xC9),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_161F',
    )

    Talk(
        (
            'RAM Load\n',
            'completed!',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_E9(0x02)

    def _loc_161F(): pass

    label('loc_161F')

    Talk(
        (
            'RAM Delete\n',
            'completed!',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_E9(0x00)

    Jump('loc_165A')

    def _loc_163F(): pass

    label('loc_163F')

    Call(0, 0x000C)

    Jump('loc_165A')

    def _loc_1646(): pass

    label('loc_1646')

    Call(0, 0x000D)

    Jump('loc_165A')

    def _loc_164D(): pass

    label('loc_164D')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_165A')

    def _loc_165A(): pass

    label('loc_165A')

    Jump('loc_D18')

    def _loc_165D(): pass

    label('loc_165D')

    OP_5F(0x0000)
    OP_56(0x00)
    OP_DA()
    Sleep(300)

    EventEnd(0x00)

    Return()

# id: 0x000C offset: 0x166B
@scena.Code('func_0C_166B')
def func_0C_166B():
    EventBegin(0x00)
    OP_5F(0x0000)
    OP_5F(0x0001)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0208, 2, 0x1042)),
            Expr.Return,
        ),
        'loc_16A3',
    )

    Talk(
        (
            'Equipment\n',
            'has been carried over!',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_16C4')

    def _loc_16A3(): pass

    label('loc_16A3')

    Talk(
        (
            'Equipment\n',
            'not carried over?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_16C4(): pass

    label('loc_16C4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0208, 3, 0x1043)),
            Expr.Return,
        ),
        'loc_16F1',
    )

    Talk(
        (
            'Items\n',
            'have been carried over!',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_170E')

    def _loc_16F1(): pass

    label('loc_16F1')

    Talk(
        (
            'Items\n',
            'not carried over?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_170E(): pass

    label('loc_170E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0208, 5, 0x1045)),
            Expr.Return,
        ),
        'loc_173B',
    )

    Talk(
        (
            'Status\n',
            'has been carried over!',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_1759')

    def _loc_173B(): pass

    label('loc_173B')

    Talk(
        (
            'Status\n',
            'not carried over?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_1759(): pass

    label('loc_1759')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0208, 6, 0x1046)),
            Expr.Return,
        ),
        'loc_1784',
    )

    Talk(
        (
            'Mira\n',
            'has been carried over!',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_17A0')

    def _loc_1784(): pass

    label('loc_1784')

    Talk(
        (
            'Mira\n',
            'not carried over?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_17A0(): pass

    label('loc_17A0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0208, 4, 0x1044)),
            Expr.Return,
        ),
        'loc_17CF',
    )

    Talk(
        (
            'Notebook\n',
            'has been carried over!',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_17EF')

    def _loc_17CF(): pass

    label('loc_17CF')

    Talk(
        (
            'Notebook\n',
            'not carried over?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_17EF(): pass

    label('loc_17EF')

    If(
        (
            (Expr.Eval, "OP_40(0x0208, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            (Expr.Eval, "OP_40(0x035C, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_1837',
    )

    Talk(
        (
            'FC Clear Data\n',
            'has been carried over!',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_185C')

    def _loc_1837(): pass

    label('loc_1837')

    Talk(
        (
            'FC Clear Data\n',
            'not carried over?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_185C(): pass

    label('loc_185C')

    Return()

# id: 0x000D offset: 0x185D
@scena.Code('func_0D_185D')
def func_0D_185D():
    EventBegin(0x00)
    OP_5F(0x0000)
    OP_5F(0x0001)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1946',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0455, 6, 0x22AE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_18DD',
    )

    Talk(
        (
            'SC Clear Data\n',
            'not carried over?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            'Since it\x27s Chapter 8,\n',
            'opening Chapter 8 Casino Shop.',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_A9(0x6C)

    Jump('loc_1943')

    def _loc_18DD(): pass

    label('loc_18DD')

    Talk(
        (
            'SC Clear Data\n',
            'has been carried over!',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            'Since it\x27s Chapter 8,\n',
            'opening Chapter 8 Casino Shop.',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_A9(0x80)

    def _loc_1943(): pass

    label('loc_1943')

    Jump('loc_1A20')

    def _loc_1946(): pass

    label('loc_1946')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0455, 6, 0x22AE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_19B6',
    )

    Talk(
        (
            'SC Clear Data\n',
            'not carried over?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            'Since it\x27s not Chapter 8,\n',
            'opening Chapter 1 Casino Shop.',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_A9(0x69)

    Jump('loc_1A20')

    def _loc_19B6(): pass

    label('loc_19B6')

    Talk(
        (
            'SC Clear Data\n',
            'has been carried over!',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            'Since it\x27s not Chapter 8,\n',
            'opening Chapter 1 Casino Shop.',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_A9(0x7D)

    def _loc_1A20(): pass

    label('loc_1A20')

    Return()

# id: 0x000E offset: 0x1A21
@scena.Code('func_0E_1A21')
def func_0E_1A21():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1CE2',
    )

    Menu(
        1,
        10,
        100,
        1,
        (
            TXT(0x00, 'Equipment\n'),
            TXT(0x01, 'Items\n'),
            TXT(0x02, 'Status\n'),
            TXT(0x03, 'Mira\n'),
            TXT(0x04, 'Notebook\n'),
            TXT(0x05, 'FC Clear Data\n'),
            TXT(0x06, 'Cancel\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)
    OP_5F(0x0001)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1A9B'),
        (0x00000001, 'loc_1AF9'),
        (0x00000002, 'loc_1B50'),
        (0x00000003, 'loc_1BA8'),
        (0x00000004, 'loc_1BFC'),
        (0x00000005, 'loc_1C58'),
        (-1, 'loc_1CD2'),
    )

    def _loc_1A9B(): pass

    label('loc_1A9B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0208, 2, 0x1042)),
            Expr.Return,
        ),
        'loc_1ACB',
    )

    Talk(
        (
            'Equipment\n',
            'has been carried over!',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_1AEC')

    def _loc_1ACB(): pass

    label('loc_1ACB')

    Talk(
        (
            'Equipment\n',
            'not carried over?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_1AEC(): pass

    label('loc_1AEC')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1CDF')

    def _loc_1AF9(): pass

    label('loc_1AF9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0208, 3, 0x1043)),
            Expr.Return,
        ),
        'loc_1B26',
    )

    Talk(
        (
            'Items\n',
            'have been carried over!',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_1B43')

    def _loc_1B26(): pass

    label('loc_1B26')

    Talk(
        (
            'Items\n',
            'not carried over?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_1B43(): pass

    label('loc_1B43')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1CDF')

    def _loc_1B50(): pass

    label('loc_1B50')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0208, 5, 0x1045)),
            Expr.Return,
        ),
        'loc_1B7D',
    )

    Talk(
        (
            'Status\n',
            'has been carried over!',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_1B9B')

    def _loc_1B7D(): pass

    label('loc_1B7D')

    Talk(
        (
            'Status\n',
            'not carried over?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_1B9B(): pass

    label('loc_1B9B')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1CDF')

    def _loc_1BA8(): pass

    label('loc_1BA8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0208, 6, 0x1046)),
            Expr.Return,
        ),
        'loc_1BD3',
    )

    Talk(
        (
            'Mira\n',
            'has been carried over!',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_1BEF')

    def _loc_1BD3(): pass

    label('loc_1BD3')

    Talk(
        (
            'Mira\n',
            'not carried over?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_1BEF(): pass

    label('loc_1BEF')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1CDF')

    def _loc_1BFC(): pass

    label('loc_1BFC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0208, 4, 0x1044)),
            Expr.Return,
        ),
        'loc_1C2B',
    )

    Talk(
        (
            'Notebook\n',
            'has been carried over!',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_1C4B')

    def _loc_1C2B(): pass

    label('loc_1C2B')

    Talk(
        (
            'Notebook\n',
            'not carried over?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_1C4B(): pass

    label('loc_1C4B')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1CDF')

    def _loc_1C58(): pass

    label('loc_1C58')

    If(
        (
            (Expr.Eval, "OP_40(0x0208, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            (Expr.Eval, "OP_40(0x035C, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_1CA0',
    )

    Talk(
        (
            'FC Clear Data\n',
            'has been carried over!',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_1CC5')

    def _loc_1CA0(): pass

    label('loc_1CA0')

    Talk(
        (
            'FC Clear Data\n',
            'not carried over?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_1CC5(): pass

    label('loc_1CC5')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1CDF')

    def _loc_1CD2(): pass

    label('loc_1CD2')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1CDF')

    def _loc_1CDF(): pass

    label('loc_1CDF')

    Jump('func_0E_1A21')

    def _loc_1CE2(): pass

    label('loc_1CE2')

    Return()

# id: 0x000F offset: 0x1CE3
@scena.Code('func_0F_1CE3')
def func_0F_1CE3():
    Talk(
        (
            TxtCtl.ShowAll,
            '请选择测试地图哦。',
            TxtCtl.Enter,
        ),
    )

    def _loc_1CF9(): pass

    label('loc_1CF9')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1E1D',
    )

    Menu(
        1,
        10,
        100,
        1,
        (
            TXT(0x00, '测试地图20\n'),
            TXT(0x01, '测试地图21\n'),
            TXT(0x02, '测试地图22\n'),
            TXT(0x03, '测试地图23\n'),
            TXT(0x04, '测试地图24\n'),
            TXT(0x05, '测试地图25\n'),
            TXT(0x06, '测试地图26\n'),
            TXT(0x07, '测试地图27\n'),
            TXT(0x08, '测试地图28\n'),
            TXT(0x09, '测试地图29\n'),
            TXT(0x0A, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1DB6'),
        (0x00000001, 'loc_1DBF'),
        (0x00000002, 'loc_1DC8'),
        (0x00000003, 'loc_1DD1'),
        (0x00000004, 'loc_1DDA'),
        (0x00000005, 'loc_1DE3'),
        (0x00000006, 'loc_1DEC'),
        (0x00000007, 'loc_1DF5'),
        (0x00000008, 'loc_1DFE'),
        (0x00000009, 'loc_1E07'),
        (-1, 'loc_1E10'),
    )

    def _loc_1DB6(): pass

    label('loc_1DB6')

    NewScene('ED6_DT21/T0020._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1DBF(): pass

    label('loc_1DBF')

    NewScene('ED6_DT21/T0021._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1DC8(): pass

    label('loc_1DC8')

    NewScene('ED6_DT21/T0022._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1DD1(): pass

    label('loc_1DD1')

    NewScene('ED6_DT21/T0023._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1DDA(): pass

    label('loc_1DDA')

    NewScene('ED6_DT21/T0024._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1DE3(): pass

    label('loc_1DE3')

    NewScene('ED6_DT21/T0025._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1DEC(): pass

    label('loc_1DEC')

    NewScene('ED6_DT21/T0026._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1DF5(): pass

    label('loc_1DF5')

    NewScene('ED6_DT21/T0027._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1DFE(): pass

    label('loc_1DFE')

    NewScene('ED6_DT21/T0028._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1E07(): pass

    label('loc_1E07')

    NewScene('ED6_DT21/T0029._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1E10(): pass

    label('loc_1E10')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1CF9')

    def _loc_1E1D(): pass

    label('loc_1E1D')

    OP_5F(0x0001)
    OP_56(0x00)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0010 offset: 0x1E2D
@scena.Code('func_10_1E2D')
def func_10_1E2D():
    Talk(
        (
            TxtCtl.ShowAll,
            '哪个？',
            TxtCtl.Enter,
        ),
    )

    def _loc_1E37(): pass

    label('loc_1E37')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1E99',
    )

    Menu(
        1,
        10,
        100,
        1,
        (
            TXT(0x00, '地图目标1\n'),
            TXT(0x01, '地图目标2\n'),
            TXT(0x02, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1E7A'),
        (0x00000001, 'loc_1E83'),
        (-1, 'loc_1E8C'),
    )

    def _loc_1E7A(): pass

    label('loc_1E7A')

    NewScene('ED6_DT21/T0070._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1E83(): pass

    label('loc_1E83')

    NewScene('ED6_DT21/T0071._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1E8C(): pass

    label('loc_1E8C')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1E37')

    def _loc_1E99(): pass

    label('loc_1E99')

    OP_5F(0x0001)
    OP_56(0x00)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0011 offset: 0x1EA9
@scena.Code('func_11_1EA9')
def func_11_1EA9():
    CameraSetDistance(5000, 3000)
    Call(0, 0x0012)

    Return()

# id: 0x0012 offset: 0x1EB7
@scena.Code('func_12_1EB7')
def func_12_1EB7():
    OP_6C(0, 20000)

    Return()

# id: 0x0013 offset: 0x1EC1
@scena.Code('func_13_1EC1')
def func_13_1EC1():
    If(
        (
            (Expr.PushValueByIndex, 0x13),
            (Expr.PushLong, 0x382),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1F0A',
    )

    EventBegin(0x00)
    OP_C2()

    If(
        (
            (Expr.Eval, "OP_CD(0x0009)"),
            Expr.Return,
        ),
        'loc_1EF7',
    )

    Sleep(1000)

    OP_62(0x0000, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)

    Jump('loc_1F05')

    def _loc_1EF7(): pass

    label('loc_1EF7')

    Talk(
        (
            '没有反应',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_1F05(): pass

    label('loc_1F05')

    EventEnd(0x00)

    Jump('loc_1F28')

    def _loc_1F0A(): pass

    label('loc_1F0A')

    Talk(
        (
            '什么也没有发生(ByScript)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    def _loc_1F28(): pass

    label('loc_1F28')

    Return()

# id: 0x0014 offset: 0x1F29
@scena.Code('func_14_1F29')
def func_14_1F29():
    ChrTalk(
        0x0000,
        (
            '欢迎',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_A9(0x00)

    Return()

# id: 0x0015 offset: 0x1F38
@scena.Code('func_15_1F38')
def func_15_1F38():
    TalkSetChrName('Sara')

    Talk(
        (
            TxtCtl.ShowAll,
            '哪个店？',
            TxtCtl.Enter,
        ),
    )

    Menu(
        1,
        10,
        100,
        1,
        (
            TXT(0x00, '工房\n'),
            TXT(0x01, '武器店\n'),
            TXT(0x02, '道具店\n'),
            TXT(0x03, '旅店\n'),
            TXT(0x04, '协会\n'),
            TXT(0x05, '读书（利贝尔通讯１）\n'),
            TXT(0x06, '娱乐场交换处\n'),
            TXT(0x07, '取消\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)
    OP_5F(0x0001)
    OP_56(0x00)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1FC7'),
        (0x00000001, 'loc_1FCE'),
        (0x00000002, 'loc_1FD5'),
        (0x00000003, 'loc_1FDC'),
        (0x00000004, 'loc_1FE3'),
        (0x00000005, 'loc_1FEA'),
        (0x00000006, 'loc_1FF2'),
        (-1, 'loc_1FF9'),
    )

    def _loc_1FC7(): pass

    label('loc_1FC7')

    Call(0, 0x0014)

    Jump('loc_1FFC')

    def _loc_1FCE(): pass

    label('loc_1FCE')

    Call(0, 0x0016)

    Jump('loc_1FFC')

    def _loc_1FD5(): pass

    label('loc_1FD5')

    Call(0, 0x0017)

    Jump('loc_1FFC')

    def _loc_1FDC(): pass

    label('loc_1FDC')

    Call(0, 0x0018)

    Jump('loc_1FFC')

    def _loc_1FE3(): pass

    label('loc_1FE3')

    Call(0, 0x0019)

    Jump('loc_1FFC')

    def _loc_1FEA(): pass

    label('loc_1FEA')

    OP_B8(0x0347, 0x0000)

    Jump('loc_1FFC')

    def _loc_1FF2(): pass

    label('loc_1FF2')

    Call(0, 0x001A)

    Jump('loc_1FFC')

    def _loc_1FF9(): pass

    label('loc_1FF9')

    Jump('loc_1FFC')

    def _loc_1FFC(): pass

    label('loc_1FFC')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0016 offset: 0x2007
@scena.Code('func_16_2007')
def func_16_2007():
    ChrTalk(
        0x0000,
        (
            '欢迎光临武器店！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_A9(0x01)

    Return()

# id: 0x0017 offset: 0x2022
@scena.Code('func_17_2022')
def func_17_2022():
    ChrTalk(
        0x0000,
        (
            '欢迎光临道具店！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_A9(0x02)

    Return()

# id: 0x0018 offset: 0x203D
@scena.Code('func_18_203D')
def func_18_203D():
    ChrTalk(
        0x0000,
        (
            '欢迎光临旅店！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_A9(0x05)

    Return()

# id: 0x0019 offset: 0x2056
@scena.Code('func_19_2056')
def func_19_2056():
    ChrTalk(
        0x0000,
        (
            '欢迎光临游击士协会！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_2A(0x0065, 0x0066, 0x0001, 0xFFFF)

    Return()

# id: 0x001A offset: 0x207C
@scena.Code('func_1A_207C')
def func_1A_207C():
    ChrTalk(
        0x0000,
        (
            '这里是交换所。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_A9(0x69)

    Return()

# id: 0x001B offset: 0x2095
@scena.Code('func_1B_2095')
def func_1B_2095():
    FadeOut(0, 0, -1)
    FormationReset()
    ClearScenaFlags(ScenaFlag(0x0240, 0, 0x1200))
    ClearScenaFlags(ScenaFlag(0x0240, 1, 0x1201))
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x09, 0xFF)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, 'Set Scherazard as Partner\n'),
            TXT(0x01, 'Set Agate as Partner\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2112'),
        (0x00000001, 'loc_2118'),
        (-1, 'loc_211E'),
    )

    def _loc_2112(): pass

    label('loc_2112')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_211E')

    def _loc_2118(): pass

    label('loc_2118')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_211E')

    def _loc_211E(): pass

    label('loc_211E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_213C',
    )

    Talk(
        (
            'ほげっちゃ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_2140')

    def _loc_213C(): pass

    label('loc_213C')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_2140(): pass

    label('loc_2140')

    Return()

# id: 0x001C offset: 0x2141
@scena.Code('func_1C_2141')
def func_1C_2141():
    MapClearFlags(0x00000001)
    CameraMove(106730, -1920, 53920, 0)
    Sleep(100)

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            0x00FF,
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['约修亚'],
            ChrTable['雪拉扎德'],
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            ChrTable['阿加特'],
            ChrTable['提妲'],
            ChrTable['金'],
            ChrTable['凯文神父'],
            ChrTable['亚妮拉丝'],
            ChrTable['克鲁茨'],
            ChrTable['乔丝特'],
            ChrTable['穆拉'],
            ChrTable['尤莉亚上尉'],
            ChrTable['理查德'],
            ChrTable['凯诺娜'],
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0)
    Sleep(1000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
