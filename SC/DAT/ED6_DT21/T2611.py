import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T2611_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2611   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2611.x'
    header.mapIndex       = 1
    header.bgm            = 32
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x00000000,
            dword_04        = 0x00000000,
            dword_08        = 0x00001770,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 45,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 0,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10000 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
        ('ED6_DT07/CH00024._CH', 'ED6_DT07/CH00024P._CP'),
        ('ED6_DT07/CH00054._CH', 'ED6_DT07/CH00054P._CP'),
        ('ED6_DT26/CH20311._CH', 'ED6_DT26/CH20311P._CP'),
    ]

# id: 0x10001 offset: 0xCA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '烛台',
            x                   = 8920,
            z                   = 6000,
            y                   = 27470,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1245184,
            chipIndex           = 0,
            npcIndex            = 0x01E2,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0xEA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0xEA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0xEA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 9080,
            triggerZ            = 4000,
            triggerY            = 28080,
            triggerRange        = 1300,
            actorX              = 8920,
            actorZ              = 6000,
            actorY              = 27470,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -39000,
            triggerZ            = 0,
            triggerY            = 30250,
            triggerRange        = 1300,
            actorX              = -39000,
            actorZ              = 1000,
            actorY              = 30250,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 44990,
            triggerZ            = 0,
            triggerY            = 3460,
            triggerRange        = 800,
            actorX              = 44990,
            actorZ              = 1000,
            actorY              = 3460,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 43000,
            triggerZ            = 0,
            triggerY            = 25500,
            triggerRange        = 1500,
            actorX              = 42980,
            actorZ              = 1000,
            actorY              = 25500,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -80200,
            triggerZ            = 250,
            triggerY            = 31450,
            triggerRange        = 1000,
            actorX              = -80240,
            actorZ              = 250,
            actorY              = 32100,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x19E
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x19F
@scena.Code('func_01_19F')
def func_01_19F():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0245, 1, 0x1229)),
            Expr.Return,
        ),
        'loc_1AF',
    )

    OP_10(0x05, 0x00)
    OP_10(0x17, 0x01)

    Jump('loc_1B5')

    def _loc_1AF(): pass

    label('loc_1AF')

    OP_10(0x05, 0x01)
    OP_10(0x17, 0x00)

    def _loc_1B5(): pass

    label('loc_1B5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0268, 1, 0x1341)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1C7',
    )

    OP_6F(0x000B, 0)

    Jump('loc_1CE')

    def _loc_1C7(): pass

    label('loc_1C7')

    OP_6F(0x000B, 60)

    def _loc_1CE(): pass

    label('loc_1CE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 5, 0x1225)),
            Expr.Return,
        ),
        'loc_1D9',
    )

    OP_64(0x00, 0x0001)

    def _loc_1D9(): pass

    label('loc_1D9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 5, 0x1225)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 6, 0x1226)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1E9',
    )

    OP_64(0x01, 0x0001)

    def _loc_1E9(): pass

    label('loc_1E9')

    OP_72(0x0001, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0245, 0, 0x1228)),
            Expr.Return,
        ),
        'loc_1FE',
    )

    OP_64(0x02, 0x0001)
    OP_71(0x0001, 0x0010)

    def _loc_1FE(): pass

    label('loc_1FE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0245, 1, 0x1229)),
            Expr.Return,
        ),
        'loc_209',
    )

    OP_64(0x03, 0x0001)

    def _loc_209(): pass

    label('loc_209')

    Return()

# id: 0x0002 offset: 0x20A
@scena.Code('func_02_20A')
def func_02_20A():
    UnlockAchievement(0x02, 0x01FE, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0268, 1, 0x1341)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2E7',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x000B, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['回复药'], 1)"),
            Expr.Return,
        ),
        'loc_27E',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['回复药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0268, 1, 0x1341))

    Jump('loc_2E4')

    def _loc_27E(): pass

    label('loc_27E')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['回复药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['回复药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x000B, 60)
    OP_70(0x000B, 0)

    def _loc_2E4(): pass

    label('loc_2E4')

    Jump('loc_318')

    def _loc_2E7(): pass

    label('loc_2E7')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_318(): pass

    label('loc_318')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x326
@scena.Code('func_03_326')
def func_03_326():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_340',
    )

    Call(0, 0x0007)
    FadeIn(0, 0)

    def _loc_340(): pass

    label('loc_340')

    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, 9240, 4000, 27500, 8)
    ChrSetPos(0x0105, 10120, 4000, 27470, 313)
    ChrSetPos(0x00F7, 7810, 4000, 27040, 39)
    ChrSetPos(0x0104, 9270, 4000, 26150, 7)
    ChrSetPos(0x0127, 8070, 4000, 26100, 36)
    CameraMove(9230, 4000, 27500, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x0105,
        (
            '#0060211485V#042F#4P『虚无之炎』……\n',
            '是说这个烛台吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211486V#1006F#6P确实只有这一根蜡烛\n',
            '没有点燃。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211487V好，调查看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '烛台中有卡片。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    Sleep(300)

    Fade(250)
    ChrSetChipByIndex(0x0101, 3)
    ChrSetSubChip(0x0101, 0)
    OP_0D()
    Sleep(500)

    FadeOut(300, 0, 100)
    OP_AD('ED6_DT24/C_VIS125._CH', 0x00BE, 0x0064, 0x000001F4)
    Sleep(1000)

    SetMessageWindowPos(-1, 300, -1, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0170211488V　第二个诅咒在教室\n',
            '　寻找『向南的学生』',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_AE(0x000001F4)
    Sleep(1000)

    LoadEffect(0x00, 'map\\\\mpfire6.eff')
    PlayEffect(0x00, 0xFF, 0x0101, 0, 600, 400, 0, 0, 0, 800, 800, 800, 0x00FF, 0, 0, 0, 0)
    PlaySE(134, 0x00, 0x64)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    Sleep(1000)

    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrMoveTo(0x0101, 9230, 4000, 27130, 2000, 0x00)
    Sleep(500)

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '卡片突然着火烧没了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0101,
        (
            '#0010211489V#1020F#6P哇哇……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211490V#1007F但、但是\n',
            '答对了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040211491V#030F嗯，这次是教室了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040211492V#035F明明没人才对，\n',
            '却说『向南的学生』吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)
    Sleep(400)

    ChrTalk(
        0x0105,
        (
            '#0060211493V#042F记得教室在\n',
            '左翼的１层和２层各有两间，\n',
            '应该有共计４间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_757',
    )

    ChrTalk(
        0x0106,
        (
            '#0050211494V#051F#6P好……一边看罗盘\n',
            '一边调查看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_78E')

    def _loc_757(): pass

    label('loc_757')

    ChrTalk(
        0x0103,
        (
            '#0030211495V#020F#6P一边看罗盘\n',
            '一边调查比较好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_78E(): pass

    label('loc_78E')

    OP_64(0x00, 0x0001)
    OP_65(0x01, 0x0001)
    SetScenaFlags(ScenaFlag(0x0244, 5, 0x1225))
    OP_28(0x0084, 0x01, 0x0004)
    EventEnd(0x00)

    Return()

# id: 0x0004 offset: 0x7A2
@scena.Code('func_04_7A2')
def func_04_7A2():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_7BC',
    )

    Call(0, 0x0007)
    FadeIn(0, 0)

    def _loc_7BC(): pass

    label('loc_7BC')

    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, -37320, 0, 30250, 270)
    ChrSetPos(0x00F7, -37650, 0, 31430, 225)
    ChrSetPos(0x0105, -37880, 0, 29190, 315)
    ChrSetPos(0x0104, -39220, 0, 28840, 360)
    ChrSetPos(0x0127, -38860, 0, 31650, 180)
    CameraMove(-38470, 0, 30820, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0127,
        (
            '#0280211496V#153F其他的座位都四处散乱着，\n',
            '只有这里的桌椅是放得好好的呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_8F5',
    )

    ChrTalk(
        0x0106,
        (
            '#0050211497V#050F朝向的方向也是正南……\n',
            '大概，就是说这里吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_935')

    def _loc_8F5(): pass

    label('loc_8F5')

    ChrTalk(
        0x0103,
        (
            '#0030211498V#022F朝向的方向也是正南……\n',
            '大概，就是这里吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_935(): pass

    label('loc_935')

    ChrTalk(
        0x0101,
        (
            '#0010211499V#1002F那么，调查看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '调查抽屉里发现了卡片。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    Sleep(300)

    Fade(250)
    ChrSetChipByIndex(0x0101, 3)
    ChrSetSubChip(0x0101, 0)
    OP_0D()
    Sleep(500)

    FadeOut(300, 0, 100)
    OP_AD('ED6_DT24/C_VIS126._CH', 0x00BE, 0x0064, 0x000001F4)
    Sleep(1000)

    SetMessageWindowPos(-1, 300, -1, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0170211500V　第三个诅咒在庭院\n',
            '  寻找『落下的头』',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_AE(0x000001F4)
    Sleep(1000)

    LoadEffect(0x00, 'map\\\\mpfire6.eff')
    PlayEffect(0x00, 0xFF, 0x0101, 0, 600, 400, 0, 0, 0, 800, 800, 800, 0x00FF, 0, 0, 0, 0)
    PlaySE(134, 0x00, 0x64)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    Sleep(1000)

    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '卡片突然着火烧没了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0101,
        (
            '#0010211501V#1004F哇哟……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211502V#1006F好像找对了，\n',
            '不过接下来是哪里呢?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040211503V#035F『庭园』和『落下的头』啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040211504V#030F挺夸张的，\n',
            '这也是什么比喻吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_64(0x01, 0x0001)
    SetScenaFlags(ScenaFlag(0x0244, 6, 0x1226))
    OP_28(0x0084, 0x01, 0x0008)
    ChrSetPos(0x0101, -37320, 0, 30250, 270)
    ChrSetPos(0x00F7, -37320, 0, 30250, 270)
    ChrSetPos(0x0105, -37320, 0, 30250, 270)
    ChrSetPos(0x0104, -37320, 0, 30250, 270)
    ChrSetPos(0x0127, -37320, 0, 30250, 270)
    CameraMove(-37320, 0, 30250, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0005 offset: 0xC62
@scena.Code('func_05_C62')
def func_05_C62():
    EventBegin(0x00)
    Fade(1000)
    CameraMove(44710, 0, 3440, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ChrSetPos(0x0101, 44390, 0, 2910, 0)
    ChrSetPos(0x00F7, 43210, 0, 2890, 45)
    ChrSetPos(0x0105, 45590, 0, 2820, 315)
    ChrSetPos(0x0104, 45160, 0, 1650, 0)
    ChrSetPos(0x0127, 43950, 0, 1770, 0)
    OP_0D()
    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门上着锁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 7, 0x1227)),
            Expr.Return,
        ),
        'loc_DF7',
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
            TXT(0x00, '【使用后门的钥匙】\n'),
            TXT(0x01, '【使用旧钥匙】\n'),
            TXT(0x02, '【不使用】\n'),
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
        (0x00000000, 'loc_DA1'),
        (0x00000001, 'loc_DC1'),
        (0x00000002, 'loc_DE8'),
        (-1, 'loc_DF4'),
    )

    def _loc_DA1(): pass

    label('loc_DA1')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '钥匙不相合。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    Jump('loc_DF4')

    def _loc_DC1(): pass

    label('loc_DC1')

    FadeIn(300, 0)
    Sleep(500)

    PlaySE(115, 0x00, 0x64)
    Sleep(1000)

    OP_64(0x02, 0x0001)
    OP_71(0x0001, 0x0010)
    SetScenaFlags(ScenaFlag(0x0245, 0, 0x1228))

    Jump('loc_DF4')

    def _loc_DE8(): pass

    label('loc_DE8')

    FadeIn(300, 0)

    Jump('loc_DF4')

    def _loc_DF4(): pass

    label('loc_DF4')

    Jump('loc_E62')

    def _loc_DF7(): pass

    label('loc_DF7')

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
            TXT(0x00, '【使用后门的钥匙】\n'),
            TXT(0x01, '【不使用】\n'),
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
        (0x00000000, 'loc_E45'),
        (-1, 'loc_E59'),
    )

    def _loc_E45(): pass

    label('loc_E45')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '钥匙不相合。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_E59(): pass

    label('loc_E59')

    FadeIn(300, 0)
    def _loc_E62(): pass

    label('loc_E62')

    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x00)

    Return()

# id: 0x0006 offset: 0xE6E
@scena.Code('func_06_E6E')
def func_06_E6E():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_E88',
    )

    Call(0, 0x0007)
    FadeIn(0, 0)

    def _loc_E88(): pass

    label('loc_E88')

    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, 43100, 0, 22930, 0)
    ChrSetPos(0x00F7, 41900, 0, 23180, 0)
    ChrSetPos(0x0105, 44610, 0, 23420, 315)
    ChrSetPos(0x0104, 43520, 0, 21510, 8)
    ChrSetPos(0x0127, 41550, 0, 21200, 17)
    CameraMove(43080, 0, 25000, 0)
    OP_67(0, 7280, -10000, 0)
    CameraSetDistance(1180, 0)
    OP_6C(35000, 0)
    OP_6E(688, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010211513V#1004F好像是……龙的雕像呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211514V#040F#2P这个雕像记得以前\n',
            '就放在这里了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211515V好像是以前在利贝尔栖息的\n',
            '古代龙的塑像……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_10C8',
    )

    ChrTalk(
        0x0106,
        (
            '#0050211516V#053F哼，真有品。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050211517V#050F总之，调查看看\n',
            '有没有什么机关吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0106, 43100, 0, 24000, 2000, 0x00)
    ChrSetDirection(0x0106, 0, 400)
    Sleep(1000)

    ChrSetDirection(0x0106, 45, 400)
    Sleep(1000)

    ChrSetDirection(0x0106, 315, 400)
    Sleep(1000)

    ChrSetDirection(0x0106, 0, 400)
    Sleep(1000)

    Fade(500)
    ChrSetFlags(0x0106, 0x0002)
    ChrSetChipByIndex(0x0106, 2)
    ChrSetSubChip(0x0106, 1)
    OP_0D()
    Sleep(1000)

    OP_62(0x0106, 0xFFFFFED4, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0106,
        (
            '#0050211518V#051F#5P……是这个了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11B9')

    def _loc_10C8(): pass

    label('loc_10C8')

    ChrTalk(
        0x0103,
        (
            '#0030211519V#026F唔，有感觉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030211520V#020F总之，调查看看\n',
            '有没有什么机关吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0103, 43100, 0, 24000, 2000, 0x00)
    ChrSetDirection(0x0103, 0, 400)
    Sleep(1000)

    ChrSetDirection(0x0103, 45, 400)
    Sleep(1000)

    ChrSetDirection(0x0103, 315, 400)
    Sleep(1000)

    ChrSetDirection(0x0103, 0, 400)
    Sleep(1000)

    Fade(500)
    ChrSetFlags(0x0103, 0x0002)
    ChrSetChipByIndex(0x0103, 1)
    ChrSetSubChip(0x0103, 1)
    OP_0D()
    Sleep(1000)

    OP_62(0x0103, 0xFFFFFED4, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0103,
        (
            '#0030211521V#027F#5P中啦㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11B9(): pass

    label('loc_11B9')

    PlaySE(130, 0x00, 0x64)
    Sleep(1000)

    FadeOut(300, 0, -1)
    OP_0D()
    PlaySE(112, 0x00, 0x64)
    Sleep(4000)

    FadeIn(300, 0)
    ChrClearFlags(0x0106, 0x0002)
    ChrClearFlags(0x0103, 0x0002)
    ChrSetChipByIndex(0x0103, 65535)
    ChrSetChipByIndex(0x0106, 65535)
    ChrSetSubChip(0x0103, 0)
    ChrSetSubChip(0x0106, 0)
    ChrSetPos(0x0101, 43100, 0, 47930, 0)
    ChrSetPos(0x00F7, 41900, 0, 48180, 0)
    ChrSetPos(0x0105, 44610, 0, 48420, 315)
    ChrSetPos(0x0104, 43380, 0, 46320, 0)
    ChrSetPos(0x0127, 41690, 0, 46310, 0)
    CameraMove(43080, 0, 48770, 0)
    OP_67(0, 7280, -10000, 0)
    CameraSetDistance(1180, 0)
    OP_6C(35000, 0)
    OP_6E(688, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x0105,
        (
            '#0060211522V#044F竟、竟然有这种东西\n',
            '在雕像底下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040211523V#030F呼……品味不错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040211524V总觉得\n',
            '相当张扬啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0127,
        (
            '#0280211525V#151F是啊～\n',
            '服务精神满满呢～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280211526V要是在旅游名胜\n',
            '说不定还能聚集客人～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211527V#1015F不过……\n',
            '我刚刚就在想。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211528V卡片什么的\n',
            '要说是幽灵作祟不是很奇怪？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_146B',
    )

    FadeOut(300, 0, 100)

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
            TXT(0x00, '【◇烛台失窃任务没有完成】\n'),
            TXT(0x01, '【◇烛台失窃任务完成了】\n'),
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
        (0x00000000, 'loc_1452'),
        (0x00000001, 'loc_145A'),
        (-1, 'loc_1462'),
    )

    def _loc_1452(): pass

    label('loc_1452')

    OP_28(0x0057, 0x03, 0x10)

    Jump('loc_1462')

    def _loc_145A(): pass

    label('loc_145A')

    OP_28(0x0057, 0x04, 0x10)

    Jump('loc_1462')

    def _loc_1462(): pass

    label('loc_1462')

    FadeIn(300, 0)

    def _loc_146B(): pass

    label('loc_146B')

    ChrTurnDirection(0x0105, 0x0101, 400)

    If(
        (
            (Expr.Eval, "OP_29(0x0057, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_1558',
    )

    ChrTalk(
        0x0105,
        (
            '#0060211529V#047F确实，没有实体的灵\n',
            '不大可能做这种事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211530V#049F而且刚才的谜题\n',
            '总觉得有印象似的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010211531V#1004F#6P啊，科洛丝也是？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211532V#1007F我也觉得这势头\n',
            '好像在哪有印象……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_159B')

    def _loc_1558(): pass

    label('loc_1558')

    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060211533V#043F确实，没有实体的灵\n',
            '不大可能做这种事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_159B(): pass

    label('loc_159B')

    ChrTurnDirection(0x00F7, 0x0101, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1608',
    )

    ChrTalk(
        0x0106,
        (
            '#0050211534V#057F无论如何\n',
            '都不是能用常理来对付的对手。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050211535V小心谨慎地下去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1664')

    def _loc_1608(): pass

    label('loc_1608')

    ChrTalk(
        0x0103,
        (
            '#0030211536V#022F无论如何\n',
            '都不是能用常理来对付的对手。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030211537V小心谨慎地下去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1664(): pass

    label('loc_1664')

    SetScenaFlags(ScenaFlag(0x0245, 1, 0x1229))
    OP_28(0x0084, 0x01, 0x0020)
    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(44540, 0, 50140, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ChrSetPos(0x0101, 44540, 0, 50140, 0)
    ChrSetPos(0x00F7, 44540, 0, 50140, 0)
    ChrSetPos(0x0105, 44540, 0, 50140, 0)
    ChrSetPos(0x0104, 44540, 0, 50140, 0)
    ChrSetPos(0x0127, 44540, 0, 50140, 0)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0007 offset: 0x171B
@scena.Code('func_07_171B')
def func_07_171B():
    FadeOut(0, 0, -1)
    ClearScenaFlags(ScenaFlag(0x0240, 0, 0x1200))
    ClearScenaFlags(ScenaFlag(0x0240, 1, 0x1201))
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)

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
            TXT(0x00, '【◇选择雪拉扎德为队友】\n'),
            TXT(0x01, '【◇选择阿加特为队友】\n'),
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
        (0x00000000, 'loc_1795'),
        (0x00000001, 'loc_179B'),
        (-1, 'loc_17A1'),
    )

    def _loc_1795(): pass

    label('loc_1795')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_17A1')

    def _loc_179B(): pass

    label('loc_179B')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_17A1')

    def _loc_17A1(): pass

    label('loc_17A1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_17AF',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_17B3')

    def _loc_17AF(): pass

    label('loc_17AF')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_17B3(): pass

    label('loc_17B3')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
